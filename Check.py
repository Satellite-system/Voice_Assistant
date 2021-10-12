'''
    this is not the Main File It is just to check
    functionality of various libraries and code- Logics

'''

# import beautifulsoup3
# import google
# num_page = 3
# search_results = google.search("This is my query", num_page)
# for result in search_results:
#     print(result.description)
'''
#   It gives source code of the url
import requests
response = requests.get('https://www.youtube.com')
print(response.text)
'''
'''
from urllib.request import urlopen
'''

'''
import webbrowser
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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


if __name__ == '__main__':
    speak("Tell me the url to search")
    new = 2
    tabUrl = "https://www.google.com/search?q="

    term = take_command()
    if term=="None":
        speak("Sorry,i was unable to hear ")
    else:
        webbrowser.open(tabUrl + term, new=new)
'''

m = input()
n = input()
s = ''
for i in range(65,91):
    s+= chr(i)
ans = ''
for i in range m:
    c = s.index(i)
    x = ( c+5)%26
    ans+ = s[x]
if(sorted(n)==sorted(ans)):
    print("Yes",end='')
else:
    print("No",end='')
