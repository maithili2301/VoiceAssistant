from email.mime import audio
import imp
from unittest import result
import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit as pwt

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
       
    speak("I am jenny, how may i help you")  
    # speak("Maithili kaisa chal raha hais") 
    # speak("Namaste, me jenny hu")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='hindi-in')
        print("User said : ",query)
    
    except Exception as e:
        # print(e)

        print("Say that again please")
        return "None"
    return query

if __name__=="__main__":
    # speak("Hello Maithili")
   wishme()
   myName="Jenny"
   while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Wikipedia searching...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia..")
           
            # print(results)
            speak(results)
        
        elif 'open youtube' in query:
            # webbrowser.open("youtube.com")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")
        
        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/")
        
        elif 'photos' in query:
            photo= 'C:\\Users\\maith\OneDrive\\Pictures\\Farewell 2K22\\FAREWELL'
            webbrowser.open(photo)
            # open(photo)
        
        # elif 'chrome' in query:
        #     webbrowser.open('C:\Program Files\Google\Chrome\Application')

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is "+strTime)
        
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        
        elif 'open map'in query:
            webbrowser.open("https://maps.google.com/")
        
        elif 'video on youtube' in query:
            speak("Youtube loading...")
            query=query.replace("on youtube","")
            pwt.playonyt(query)

        elif 'play' in query:
            speak("Youtube loading...")
            query=query.replace("play","")
            pwt.playonyt(query)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you...")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'what is your name' in query:
            speak("My friends call me")
            speak("Jenny")
            print("My friends call me jenny" )

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query: 
            speak("I have been created by Maithili.")

        elif 'who created you' in query:
            speak("I have been created by Maithili")

        # elif 'calculate' in query:

