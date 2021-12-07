import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnknownValueError:
            speak('Anlayamadım Lütfen Tekrar Edebilir Misin')
        except sr.RequestError:
            speak('Sistem Çalışmıyor')
        return voice







def response(voice):
    if 'nasılsın' in voice:
        speak('İyi Senden')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
       search = record('Ne Aramak İstiyorsun')
       url = 'https://google.com/search?q='+search
       webbrowser.get().open(url)
       speak(search + ' dediğin için arattım ve bunları buldum')
    if 'Aleykümselam' in voice:
        speak('Ne yapmamı istiyorsun')
    if 'teşekkür ederim' in voice:
        speak('Allaha emanet')
        exit()


def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


    
speak('Selamunaleyküm')
time.sleep(0.3)
while  0.3:
    voice = record()
    print(voice)
    response(voice)

    
    


