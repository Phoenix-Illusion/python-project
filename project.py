import webbrowser
import speech_recognition as sr
import os
import wikipedia
import datetime
import pyjokes
import pyttsx3
import json
from urllib.request import urlopen
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query

while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open('https://www.youtube.com/')
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open('https://www.google.co.in/')
        elif 'play music' in query or "play song" in query:
            music_dir = "C:\\Users\\tiwar\\Music\\my songs"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))  
        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'powerpoint' in query:
            speak("opening Power Point presentation")
            power = r"C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(power)
        elif 'word' in query:
            speak("opening MS Word")
            word = r"C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(word)
        elif 'excel' in query:
            speak("opening MS Excel")
            excel = r"C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
            os.startfile(excel)
            print(power)
        elif 'news' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&apiKey=0511a1a5fe7049d09f3c3aa5203860a8''')
                data = json.load(jsonObj)
                i = 1
                speak('here are some top news on India')
                print('''=============== INDIA ============'''+ '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    if i>6:
                        break
            except Exception as e:
                print(str(e))
        elif 'exit' in query:
            print("Thanks for giving me your time.")
            speak("Thanks for giving me your time.")
            exit()
            