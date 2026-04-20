import speech_recognition as sr
import os
import webbrowser

def listen_command():
    r = sr.Recognizer()
    mic = sr.Microphone()

    print("Speak now...")

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand")
        return None
    except sr.RequestError as e:
        print("Request error:", e)
        return None

command = listen_command()

if command:
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")

    elif "open whatsapp" in command:
        os.system("start whatsapp:")

    elif "open telegram" in command:
        os.system("start telegram:")

    elif "open calculator" in command:
        os.system("calc")

    elif "open notepad" in command:
        os.system("notepad")

    else:
        print("Invalid command")
