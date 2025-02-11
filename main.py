from scripts.voice_recognition import VoiceRecognition
from scripts.object_detection import ObjectDetection

class Main:
    def __init__(self):

        # Store the class specified by voice recognition
        self.selected_class = ""
        # Create an instance of VoiceRecognition
        self.VoiceRecognizer = VoiceRecognition()
        # Create an instance of ObjectDetection
        self.ObjectDetector = ObjectDetection()  

    def run(self):

        # Execute voice recognition
        self.VoiceRecognizer.voice_recognition()  
        self.selected_class = self.VoiceRecognizer.recognized_keyword
        # print(self.VRec.recognized_keyword)   # Display the recognized keyword

        # Execute object detection
        self.ObjectDetector.object_detection(self.selected_class)


# Main function
def main():
    
    # Create an instance of the Main class
    app = Main()
    # Run the application
    app.run()


# Call main() if this script is executed directly
if __name__ == "__main__":
    main()
