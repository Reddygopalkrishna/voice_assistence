import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        return user_input.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error connecting to the speech recognition service.")
        return ""

def main():
    speak("Hello! How can I assist you today?")

    while True:
        user_input = listen()

        if "hello" in user_input:
            speak("Hello! How can I assist you today?")
        elif "what's your name" in user_input:
            speak("My name is Python Assistant.")
        elif "who made you" in user_input:
            speak("I was created by [Your Name].")
        elif "exit" in user_input:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't know how to respond to that.")

if __name__ == "__main__":
    main()
