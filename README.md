# 🦻 Assistive Device for Deaf People – Speech-to-Text via Bluetooth  

## 🔹 Overview  
This project is a **wearable assistive device** designed to help hearing-impaired individuals recognize speech in real-time.  

It uses:  
- Raspberry Pi 4 for audio capture and speech recognition  
- Google Speech Recognition API for speech-to-text conversion  
- Bluetooth (HC-05/HC-06) for wireless communication  
- Arduino Nano + OLED display for real-time text output  

The software listens for **user-defined wake words** (set through text input), starts transcription upon detection, and streams the transcribed text via Bluetooth for display.  

---

## 🔹 Features  
- Real-time speech-to-text conversion  
- Configurable wake words (text input only)  
- Wake word detection triggers transcription mode  
- Exit word stops transcription  
- Sends transcribed text to HC-05 Bluetooth module  
- Error handling for:  
  - Bluetooth connection  
  - Speech recognition  
  - User interruption  

---

## 🔹 Requirements  

**Software:**  
- Python 3.x  
- Libraries: `pyserial`, `SpeechRecognition`  

**Hardware:**  
- Raspberry Pi 4  
- USB Microphone  
- HC-05 Bluetooth module  
- Arduino Nano + HC-06 + OLED Display  

---

## 🔹 Usage  
1. Connect HC-05 Bluetooth to Raspberry Pi (`/dev/rfcomm0`).  
2. Run the Python script.  
3. Add wake words via text input.  
4. Speak into the microphone:  
   - Saying a wake word starts transcription  
   - Saying **exit** stops transcription  
5. All recognized speech is transmitted to Arduino Nano for display on OLED.  

---

## 🔹 Applications  
- Hearing aid for deaf and hard-of-hearing individuals  
- Inclusive communication in classrooms, workplaces, and daily life  
- Emergency alert awareness  
