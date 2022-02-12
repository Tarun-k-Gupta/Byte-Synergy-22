import time
import os

def botSpeak(data):
    with open("botSpeech.txt", 'w') as bS:
        bS.write(data)
    os.system("python3 botSpeak.py")
    os.system("python3 playAudio.py")

currentTime = time.strftime("%H:%M:%S")
lst=currentTime.split(":")
totMins = int(lst[0])*60 + int(lst[1])
greetText = ""
if (totMins >= 300 and totMins <= 719):
    greetText = "Good Morning"
elif (totMins >= 720 and totMins <= 1019):
    greetText = "Good Afternoon"
else:
	greetText = "Good Evening"

botSpeak(greetText)
print(greetText+"!")
botSpeak("How can I help you?")
print("How can I help you?")

os.system("python3 botListen.py")
os.system("python3 interpretAudio.py")
os.system("python3 interpretInputText.py")