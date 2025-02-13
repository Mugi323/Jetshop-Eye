import os
import cv2
import time
from ultralytics import YOLO
import numpy as np
from playsound import playsound
import threading


class ObjectDetection:
    def __init__(self):
        # Specify model directory
        self.model_path = "./models/YOLOv8n.pt"
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"YOLO model file not found: {self.model_path}")
        
        # Load the pre-trained model
        self.model = YOLO(self.model_path)
        
        # List of class names
        # This list defines the categories (classes) used in an image recognition or classification model.
        # In this example, the model classifies images into five categories: "Onigiri" (rice ball), 
        # "Bread", "Ramen", "Bottle", and "Snack".        
        self.class_names = ['おにぎり', 'パン', 'ラーメン', 'ボトル', '菓子']
        
        # Initialize camera settings
        self.cap = cv2.VideoCapture(0)  # Select default camera (0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        # Dictionary mapping positions to corresponding audio files
        self.sounds = {
            "left": "./audio/left.wav",
            "right": "./audio/right.wav",
            "upper": "./audio/upper.wav",
            "lower": "./audio/lower.wav",
            "right_upper": "./audio/right_upper.wav",
            "left_upper": "./audio/left_upper.wav",
            "right_lower": "./audio/right_lower.wav",
            "left_lower": "./audio/left_lower.wav",
            "center": "./audio/center.wav",
        }
        
        self.currently_playing = None  # Track currently playing sound
        self.last_played_time = 0  # Track last played sound time

    def play_sound(self, position):
        """Plays sound asynchronously with a 1-second interval restriction"""
        current_time = time.time()
        if position in self.sounds and self.currently_playing != position and (current_time - self.last_played_time) >= 1:
            self.currently_playing = position
            self.last_played_time = current_time
            sound_path = self.sounds[position]

            def play_and_reset():
                playsound(sound_path)
                self.currently_playing = None  # Reset after playing

            # Play sound in a separate thread
            threading.Thread(target=play_and_reset, daemon=True).start()

    def object_detection(self, selected_class):
        """Detects the selected object and determines its relative position to a detected hand."""
        if selected_class not in self.class_names:
            raise ValueError(f"Invalid class name: {selected_class}")

        # Retrieve class ID from class names
        selected_class_id = self.class_names.index(selected_class)

        # Initialize hand coordinates
        hand_x1, hand_y1, hand_x2, hand_y2 = -1, -1, -1, -1
        hand_detection = False

        # Initialize detected object coordinates
        merchandise_x1, merchandise_y1, merchandise_x2, merchandise_y2 = -1, -1, -1, -1
        merchandise_detection = False

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to retrieve frame from camera.")
                break

            results = self.model(frame)

            detected_position = None
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    cls = int(box.cls[0])

                    # Detect hand (assumed to have class ID 5)
                    if cls == 5:
                        hand_x1, hand_y1, hand_x2, hand_y2 = map(int, box.xyxy[0])
                        hand_detection = all(coord > 0 for coord in [hand_x1, hand_y1, hand_x2, hand_y2])
                    # Detect selected object
                    elif cls == selected_class_id:
                        merchandise_x1, merchandise_y1, merchandise_x2, merchandise_y2 = map(int, box.xyxy[0])
                        merchandise_detection = all(coord > 0 for coord in [merchandise_x1, merchandise_y1, merchandise_x2, merchandise_y2])

            if hand_detection and merchandise_detection:
                # Calculate the center of the hand and the object
                hand_center_x = (hand_x1 + hand_x2) // 2
                hand_center_y = (hand_y1 + hand_y2) // 2
                box_center_x = (merchandise_x1 + merchandise_x2) // 2
                box_center_y = (merchandise_y1 + merchandise_y2) // 2

                threshold_x = 200
                threshold_y = 200

                # Determine horizontal position
                if box_center_x < hand_center_x - threshold_x:
                    horizontal_position = "left"
                elif box_center_x > hand_center_x + threshold_x:
                    horizontal_position = "right"
                else:
                    horizontal_position = "center"

                # Determine vertical position
                if box_center_y < hand_center_y - threshold_y:
                    vertical_position = "upper"
                elif box_center_y > hand_center_y + threshold_y:
                    vertical_position = "lower"
                else:
                    vertical_position = "center"

                detected_position = None

                # Determine final detected position
                if horizontal_position == "left" and vertical_position == "upper":
                    detected_position = "left_upper"
                elif horizontal_position == "left" and vertical_position == "lower":
                    detected_position = "left_lower"
                elif horizontal_position == "right" and vertical_position == "upper":
                    detected_position = "right_upper"
                elif horizontal_position == "right" and vertical_position == "lower":
                    detected_position = "right_lower"
                elif horizontal_position == "center" and vertical_position == "upper":
                    detected_position = "upper"
                elif horizontal_position == "center" and vertical_position == "lower":
                    detected_position = "lower"
                elif horizontal_position == "left" and vertical_position == "center":
                    detected_position = "left"
                elif horizontal_position == "right" and vertical_position == "center":
                    detected_position = "right"
                else:
                    detected_position = "center"

                print(f"Detected position: {detected_position}")

                # Play corresponding sound (limited to 1-second intervals)
                if detected_position:
                    self.play_sound(detected_position)
                    if detected_position == "center":
                        print("Center detected. Stopping detection.")
                        break
                    
                    # Reset detection variables
                    hand_x1, hand_y1, hand_x2, hand_y2 = -1, -1, -1, -1
                    hand_detection = False

                    merchandise_x1, merchandise_y1, merchandise_x2, merchandise_y2 = -1, -1, -1, -1
                    merchandise_detection = False
                    detected_position = None

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
