import datetime
import os
import random
import smtplib
import webbrowser

import speech_recognition as sr

import pyttsx3
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("jarvismypersonalai474@gmail.com", 'abcde&12345')
    server.sendmail('jarvismypersonalai474@gmail.com',to,content)
    server.close()
    return


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis at you Service Sir!!,How can i help you ?")
    return


def take_command():
    # take input from upper microphone and change that to a string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:  {query} \n")
    except Exception as e:
        print(e)
        print("say that Again Please...")
        return "None"
    return query

def googleSearch():
    new = 2
    tabUrl = "https://www.google.com/search?q="
    term = take_command()
    repeat = False
    if term == "None":
        speak("Sorry,i was unable to hear ")
        speak("will you repeat ?")
        whetherRepeat = take_command()
        if whetherRepeat == "no":
            return
        else:
            googleSearch()

    else:
        webbrowser.open(tabUrl + term, new=new)


if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()
        # logic for executing task based upon query
        if 'wikipedia' in query:
            speak('Seaching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'music' in query:
            music_dir = 'C:\\Users\\adars\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)
            n = random.choice(songs)
            os.startfile(os.path.join(music_dir, n))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'opera' in query:
            codePath = "C:\\Users\\adars\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath)
        elif 'what is your name' in query:
            str = "My name's ,Jarvis your personal voice assistant."
            speak(str)
            str = "I just wish that ,everyone had a nickname ,as cool as mine."
            speak(str)
        elif 'send mail' in query:
            try:
                speak("What should i send ?")
                content = take_command()
                to = "zakarian17s@gmail.com"
                sendEmail(to, content)
                speak("Email has been send, Sir")
            except Exception as e:
                print(e)
                speak("Sorry Sir , I am unable to send this mail")
        elif 'quit' in query:
            break
        elif 'search' in query:
            speak("Sure To find info about Something")
            speak("Just say")
            googleSearch()
            break

        elif 'wait' in query:
            speak("No rush! Take your time")

        elif 'hello' in query:
            speak("hii it's good to hear from you.")
            speak("I hope you and your loved ones are staying safe and healthy during this difficult time.")
        elif 'how are you' in query:
            speak("i'm fine,thanks for asking")
            speak("This is a challenging time for us.")
            speak("I hope you and your loved ones are staying safe and healthy")
