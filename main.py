from scripts.voice_recognition import VoiceRecognition
from scripts.object_detection import ObjectDetection

class Main:
    def __init__(self):

        # Store the class specified by voice recognition
        self.selected_class = ""
        # Create an instance of VoiceRecognition
        self.voice_recognizer = VoiceRecognition()
        # Create an instance of ObjectDetection
        self.object_detector = ObjectDetection()  

    def run(self):

        # Execute voice recognition
        self.voice_recognizer.voice_recognition()  
        self.selected_class = self.voice_recognizer.recognized_keyword
        # print(self.VRec.recognized_keyword)   # Display the recognized keyword

        # Execute object detection
        self.object_detector.object_detection(self.selected_class)


# Main function
def main():
    
    # Create an instance of the Main class
    app = Main()
    # Run the application
    app.run()


# Call main() if this script is executed directly
if __name__ == "__main__":
    main()
