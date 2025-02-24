# Jetshop Eye

## Overview

This project integrates speech recognition and object detection into a Python application.
When a user specifies a product name using voice commands, the system detects the product through the camera and provides audio feedback about its location.

This application utilizes Vosk for speech recognition and YOLOv8 for object detection.

**This application is designed for Jetson devices and has been developed using Jetson Orin Nano.**

## Installation

### Requirements

- Jetson Orin Nano
- Ubuntu
- Python 3.8 or later
- Required libraries
- Webcam
- Headset with a microphone

### Setup Instructions

1. Clone the repository:
    
    ```
    git clone https://github.com/user/object-detection-voice.git
    cd object-detection-voice
    ```
    
2. Install dependencies:
    
    ```
    pip install -r requirements.txt
    ```
    
3. Run the application:
    
    ```
    python main.py
    ```
    

## Usage

1. Connect the webcam and headset to Jetson. The user must wear the headset and wear the webcam around his/her neck.
2. Start the application; it will prompt for voice input.
3. **Speak in Japanese** and specify the name of an object you want to detect. The system recognizes the following keywords: **「おにぎり」 (rice ball), 「パン」 (bread), 「ラーメン」 (ramen), 「ボトル」 (bottle), and 「菓子」 (snack).**
4. The camera will detect the specified object and provide voice guidance about its relative position.

⚠ **Note**: This application **only recognizes Japanese**. Other languages are not supported.

## Directory Structure

```
📦 Jetshop-Eye
┣ 📂 scripts
┃ ┣ 📜 voice_recognition.py
┃ ┣ 📜 object_detection.py
┣ 📂 models
┃ ┣ 📂 vosk-japanese-small
┃ ┣ 📜 YOLOv8.pt
┣ 📂 audio (contains multiple .wav files)
┣ 📜 requirements.txt
┣ 📜 README.md
```

## Demo

![Image](https://github.com/user-attachments/assets/ecefa50b-1beb-4815-89d2-93195be888a1)

## Contribution

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

- **Name**: [@Mugi323](https://github.com/Mugi323)
- **GitHub**: [@Mugi323](https://github.com/Mugi323)

