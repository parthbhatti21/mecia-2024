import speech_recognition as sr
import time
import ai
import Web1
import audio as a
from gtts import gTTS
def save_text_to_audio(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

def recognize_speech(c):
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        
        if(c==0):
            a.text_to_audio_and_play1('Good afternoon! Im AI assistant from SVIT vasad')
            
        else:
            a.text_to_audio_and_play1('Do you need more assistant?')
    
        audio = recognizer.listen(source)
    try:
        if Web1.stop_flag:
            return
        else:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            ai.ai(text=text)
        # filename="Hello.mp3"
        # save_text_to_audio(text, filename)
        # print(f"Audio saved as {filename}")
        # '''with open('example.txt', 'w') as file:
        #  file.write(text)

        # print("File created and text written successfully.")'''
    except sr.UnknownValueError:
        a.text_to_audio_and_play1('Sorry, i am not able to understand the audio.')
    except sr.RequestError as e:
        a.text_to_audio_and_play1('Sorry, i am not able to understand the audio.')

