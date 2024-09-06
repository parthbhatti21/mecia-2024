from gtts import gTTS
import pygame
import os
import Web1
def stop():
    pygame.mixer.music.stop()
count=0

def text_to_audio_and_play(text):
    try:
        global count
        tts = gTTS(text=text, lang='en')
        filename = f"output{count}.mp3"
        tts.save(filename)
        print(f"Audio file saved as {filename}")
        count+=1
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        if(Web1.stop_flag):
            return
        else:
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        
            os.remove(filename)
            print("Audio playback finished and file deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")

def text_to_audio_and_play1(text):
    try:
        global count
        tts = gTTS(text=text, lang='en')
        filename = f"output{count}.mp3"
        tts.save(filename)
        print(f"Audio file saved as {filename}")
        count+=1
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        if(Web1.stop_flag):
            return
        else:
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        
            os.remove(filename)
            print("Audio playback finished and file deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")