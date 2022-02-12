from gtts import gTTS
import os

myText = ""
with open("botSpeech.txt",'r') as s:
    myText = s.read()
myLang = 'en-in'

myAudio = gTTS(text= myText, lang= myLang, slow= False)
os.remove("botSpeech.txt")
myAudio.save("botSpeech.wav")