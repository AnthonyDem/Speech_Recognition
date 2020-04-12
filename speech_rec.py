from datetime import datetime
from gtts import gTTS
from time import ctime
import speech_recognition as sr
import webbrowser
import pyttsx3
import playsound
import os
import random
import time



tts = pyttsx3.init()
rec = sr.Recognizer()
pages = {'google.com': 'http://google.com', 'facebook': 'https://www.facebook.com',
         'linkedin': 'https://linkedin.com/home', 'github': 'https://github.com',
         'youtube': 'https://www.youtube.com'}
functionality = ['1: what is date now', '2: open url', '3: search', '4: find location', '5: exit']


def record_audio(ask=''):
    with sr.Microphone() as source:
        if ask:
            thony_speak(ask)
        audio = rec.listen(source)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(audio)
        except sr.UnknownValueError:
            thony_speak('Sorry, i didn\'t get that')
        except sr.RequestError:
            thony_speak('Srry , my speech service is down')
        return voice_data


def thony_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    rand = random.randint(1, 1000)
    audio_file = 'audio-' + str(rand) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is date now' in voice_data:
        thony_speak('Now is ' + str(datetime.now()))
    if 'open url' in voice_data:
        thony_speak('i can open different pages: ' + ','.join(pages.keys()) + ' and maybe answer on your questions ')
        voice = record_audio()
        for page in pages.keys():
            if str(page) in voice.lower():
                webbrowser.open_new(pages.get(page))
            else:
                continue
    if 'search' in voice_data:
        thony_speak('What do u want to search?')
        search = record_audio()
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        thony_speak('Here is what i found for ' + search)
    if 'find location' in voice_data:
        thony_speak('What is the location?')
        location = record_audio()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        thony_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
thony_speak('How can i help you?')
for func in functionality:
    print(func)
while 1:
    voice_data = record_audio()
    respond(voice_data)
