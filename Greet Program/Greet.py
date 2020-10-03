# Program that greets you


import datetime


import pyttsx3


def speak(audio):
    engine.say(audio);
    engine.runAndWait();


def greet():
    hour=int(datetime.datetime.now().hour);

    if (hour >= 5 and hour < 12):
        speak("Good Morning Sir")

    else:

        if (hour >= 12 and hour < 17):
            speak("Good Afternoon Sir")
        else:
            speak("Good Evening Sir");


if __name__ == '__main__':
    engine = pyttsx3.init("sapi5");
    voices = engine.getProperty('voices');
    engine.setProperty("voice", voices[1].id)

    greet();