import sounddevice as sd
import queue
import sys
import json
from vosk import Model, KaldiRecognizer
from playsound import playsound

class VoiceRecognition:
    def __init__(self):
        # Specify model directory
        self.model_path = "./models/vosk-japanese-small"
        # Load model
        try:
            self.model = Model(self.model_path)
        except Exception as e:
            print(f"Model not found: {e}")
            sys.exit(1)
        # Manage audio data using a queue
        self.q = queue.Queue()
        # List of keywords to recognize
        self.keyword_list = ["おにぎり", "パン", "ラーメン", "ボトル", "菓子"]
        # Recognized keyword
        self.recognized_keyword = ""

        # Dictionary mapping positions to corresponding audio files
        self.sounds = {
            "start_guide": "./audio/voice_recognition_start.wav",
            "stop_guide": "./audio/voice_recognition_stop.wav",
        }

    def audio_callback(self, indata, frames, time, status):
        """Adds audio data from the microphone to the queue"""
        if status:
            print(f"Status: {status}", file=sys.stderr)
        self.q.put(bytes(indata))

    def contains_keyword(self, text):
        """Checks if the recognized text contains a keyword"""
        for keyword in self.keyword_list:
            if keyword in text:
                self.recognized_keyword = keyword
                # print(self.recognized_keyword)  # Display recognized keyword
                return True
        return False

    def voice_recognition(self):
        recognizer = KaldiRecognizer(self.model, 16000)  # Recognize at 16kHz
        print("Please speak into the microphone. Press Ctrl+C to exit.")

        # Play guide audio
        playsound(self.sounds["start_guide"])

        try:
            # Open audio stream
            with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                                   channels=1, callback=self.audio_callback):
                while True:
                    data = self.q.get()
                    if recognizer.AcceptWaveform(data):
                        result = json.loads(recognizer.Result())
                        text = result.get("text", "")
                        print(f"Recognition result: {text}")

                        if self.contains_keyword(text):
                            print("Keyword detected. Ending voice recognition.")
                            # Play guide audio
                            playsound(self.sounds["stop_guide"])
                            break
                    else:
                        partial_result = json.loads(recognizer.PartialResult())
                        partial_text = partial_result.get("partial", "")
                        print(f"Partial result: {partial_text}")
        except Exception as e:
            print(f"Audio stream error: {e}")
            sys.exit(1)
