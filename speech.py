import serial
import time
import speech_recognition as sr

# Open serial communication with HC-05 (Master)
try:
    ser = serial.Serial('/dev/rfcomm0', 9600, timeout=1)  # Bluetooth serial port
    ser.flush()
    print("Connected to HC-05 via Bluetooth.")
except Exception as e:
    print(f"Bluetooth connection failed: {e}")
    exit()

# Initialize speech recognizer and microphone
recognizer = sr.Recognizer()
mic = sr.Microphone()

wake_words = []

# --- WAKE WORD UPDATE PHASE ---
print("\n--- Wake Word Update Phase ---")
print("Update wake words using text input only.")
print("Type each wake word and press Enter.")
print("Type 'done' when finished.\n")

# Text input loop for wake word collection
while True:
    spoken_text = input("Type wake word (or 'done' to finish): ").strip().lower()
    
    if spoken_text == "done":
        if not wake_words:
            print("No wake words added yet. Please add at least one.")
        else:
            print(f"Wake words set: {wake_words}")
            break
    else:
        wake_words.append(spoken_text)
        print(f"Added wake word: {spoken_text}")

# --- MAIN LOOP STARTS ---
transcription_active = False
print(f"\nWake word listening has started (speech only). Waiting for any of: {wake_words}\n")

while True:
    try:
        with mic as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")

            audio = recognizer.listen(source)
            spoken_text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {spoken_text}")

        if spoken_text in wake_words and not transcription_active:
            print(f"Wake word '{spoken_text}' detected. Starting transcription mode...")
            ser.write(f"Wake word detected: {spoken_text}\n".encode())
            transcription_active = True
            continue

        elif spoken_text == "exit" and transcription_active:
            print("Stopping transcription mode...")
            ser.write("Transcription stopped.\n".encode())
            transcription_active = False
            continue

        if transcription_active:
            print(f"Sending transcription: {spoken_text}")
            ser.write(f"{spoken_text}\n".encode())

    except sr.UnknownValueError:
        print("Could not understand the speech, try again.")
    except sr.RequestError as e:
        print(f"Speech recognition request failed: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Close Bluetooth serial connection
ser.close()
print("Bluetooth connection closed.")
