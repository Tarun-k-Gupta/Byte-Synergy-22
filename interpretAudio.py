import speech_recognition as sr
import os
import GUI

def interpretAudio(textBox):
	r = sr.Recognizer()
	file = sr.AudioFile('userSpeech.wav')
	with file as source:
		r.adjust_for_ambient_noise(source)
		audio = r.record(source)
	userText = r.recognize_google(audio)
	GUI.guiPrint(textBox,userText)
	os.remove("userSpeech.wav")
	with open("userInput.txt", 'w') as uI:
		uI.write(userText)
