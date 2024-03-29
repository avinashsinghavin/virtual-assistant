import pyttsx3
import numpy as np
import wikipedia
import datetime
import cv2
import webbrowser
import os
from googlesearch import search
import random
import smtplib
import speech_recognition as sr
from collections import defaultdict



data = defaultdict(str) 
data['shutdown'] = "sudo shutdown now"
data['close google'] = "taskkill /im chrome.exe /f"
data['wikipedia'] = "wikipedia"
data['open stackoverflow'] = "https://www.stckoverflow.com"
data['open code'] = "C:\\Users\\Avinash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
data['open youtube'] = "https://www.youtube.com"



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to,content):
    server  = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('princeofdeath25@gmail.com','.#Prince1')
    server.sendmail('princeofdeath25@gmail.com',to,content)
    server.close()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning! ")
    elif 12 <= hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening ")
    speak("I am Alex Sir, Please tell me how may I help You")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=900
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...  ")
        return "None"
    return query

def waitcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=900
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)

        return "None"
    return query


if __name__ == "__main__":
    wishme()
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.register('chrome', None)
            webbrowser.open(data['open youtube'])
        elif 'open google' in query:
            query = takeCommand().lower()
            for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
                print(j) 
                webbrowser.register('chrome', None)
                webbrowser.open(j)
            '''
            query=takeCommand().lower()
            #webbrowser.open("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            webbrowser.register('chrome', None)
            webbrowser.open(query)'''
        
        elif 'open stackoverflow' in query:
            webbrowser.register('chrome', None)
            webbrowser.open(data['open stackoverflow'])

        elif 'close google' in query:
            os.system(data['close google'])
            # fun(query)
        elif 'play music' in query:
            songs = os.listdir('F:\\Fav')
            print(songs)
            x = len(songs)-1
            p = random.randint(0,x)
            os.startfile(os.path.join('F:\\Fav',songs[23]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strtime}")
            
        elif 'open code' in query:
            path=data['open code']
            os.startfile(path)
            
            data['close code'] = 'TASKKILL /F /IM Code.exe'
        elif 'close code' in query:
            os.system(data['close code'])
            
        elif 'email to avinash' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "tigeravinash@gmail.com"
                sendEmail(to,content)
                speak("Email Has send")
            except Exception  as e:
                print(e)
                speak(" Sorry sir I am not able to  send this email ")
        
        elif 'wait' in query or 'sleep' in query or 'rest' in query:
            while True:
                print('.')
                query=waitcommand().lower()
                if 'start' in query or 'wake up' in query:
                    speak("I am always for your service sir")
                    break
        
        elif 'quit' in query or 'exit' in query:
            speak("I hope you liked my service sir, please wake me up when you need me")
            break
            
        elif 'your name' in query:
            speak(" My name is Alex")
        elif 'hello' in query:
            speak(" hello Sir, how may i help you ")
        elif 'open notepad' in query:
            cmd = 'notepad'
            os.system(cmd)
        elif 'shutdown' in query:
            os.system(data['shutdown'])
        elif 'open camera':
            cap = cv2.VideoCapture(0)
            while(True):
                # Capture frame-by-frame
                query=waitcommand().lower()
                ret, frame = cap.read()
                # Our operations on the frame come here
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # Display the resulting frame
                cv2.imshow('frame',gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                print(query)
                if 'close' in query:
                    break
            # When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()
        else :
            speak("please give me some instrucioin")