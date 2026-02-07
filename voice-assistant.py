import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your Python Voice Assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        speak("Sorry, I did not understand. Please repeat.")
        return ""

def run_assistant():
    wish()
    while True:
        query = take_command()

        if 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is {time}")

        elif 'date' in query:
            date = datetime.date.today()
            speak(f"Today's date is {date}")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif 'search' in query:
            speak("What should I search?")
            search = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search}")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a nice day.")
            break

        elif query != "":
            speak("Sorry, command not recognized")

if __name__ == "__main__":
    run_assistant()
