import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import os
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"Command recognized: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return None
        except sr.RequestError:
            speak("Sorry, I can't connect to the internet.")
            return None
        except sr.WaitTimeoutError:
            speak("No voice detected, please speak again.")
            return None

def execute_command(command):
    if 'open browser' in command:
        speak("Opening browser")
        webbrowser.open('https://www.google.com')

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open('https://www.youtube.com')

    elif 'open notepad' in command:
        speak("Opening Notepad")
        os.system('notepad')

    elif 'type hello' in command:
        speak("Typing Hello World")
        pyautogui.typewrite("Hello World!")
        pyautogui.press('enter')

    elif 'scroll down' in command:
        speak("Scrolling down")
        pyautogui.scroll(-500)

    elif 'scroll up' in command:
        speak("Scrolling up")
        pyautogui.scroll(500)

    elif 'screenshot' in command:
        speak("Taking screenshot")
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        speak("Screenshot saved")

    elif 'shutdown' in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 5")

    elif 'increase volume' in command:
        speak("Increasing volume")
        pyautogui.press('volumeup')

    elif 'decrease volume' in command:
        speak("Decreasing volume")
        pyautogui.press('volumedown')

    elif 'mute' in command:
        speak("Muting volume")
        pyautogui.press('volumemute')

    elif 'lock screen' in command:
        speak("Locking the screen")
        pyautogui.hotkey('win', 'l')

    elif 'open file explorer' in command:
        speak("Opening File Explorer")
        os.system('explorer')

    elif 'close window' in command:
        speak("Closing current window")
        pyautogui.hotkey('alt', 'f4')

    elif 'quit' in command:
        speak("Goodbye!")
        exit(0)

    else:
        speak("Command not recognized, please try again.")

def start_voice_assistant():
    speak("I am ready for your command.")
    while True:
        command = take_command()
        if command:
            execute_command(command)
        time.sleep(1)

if __name__ == "__main__":
    start_voice_assistant()
