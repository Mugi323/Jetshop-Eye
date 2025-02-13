# Jetshop Eye
## Overview

This project integrates speech recognition and object detection into a Python application.
When a user specifies an object using voice commands, the system detects the object through the camera and provides audio feedback about its location.

This application utilizes Vosk for speech recognition and YOLOv8 for object detection.

## Demo

![https://example.com/demo.gif](https://example.com/demo.gif)

## Installation

### Requirements

- Python 3.8 or later
- Required libraries

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

1. Start the application; it will prompt for voice input.
2. Speak the name of an object you want to detect, such as "rice ball," "bread," or "ramen."
3. The camera will detect the specified object and provide voice guidance about its relative position.

## Configuration

Create a `.env` file and define the following variables:

```
YOLO_MODEL_PATH=./models/YOLOv8n.pt
VOSK_MODEL_PATH=./models/vosk-japanese-small
```

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

## Contribution

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

- **Name**:
- **GitHub**: 
