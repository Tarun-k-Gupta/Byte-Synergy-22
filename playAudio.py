from playsound import playsound
import os

def playAudio():
    playsound('botSpeech.wav')
    os.remove("botSpeech.wav")
