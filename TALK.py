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

print("Please confirm that you are online.\nEnter Y to confirm:")
confirmation = input()
if(confirmation.lower()[0] == "y"):    
    botSpeak(greetText)
    print(greetText+"!")
    botSpeak("How can I help you?")
    print("How can I help you?")
    botSpeak("Would you like to give voice input? Or would you prefer typing your query here?")
    print("Would you like to give voice input?")
    print("Or would you prefer typing your query here?")
    print("Please enter V/T (V for VOICE input and T for TYPED input):")
    choice = input()
    if(choice.lower()[0] == "v"):
        botSpeak("I am listening")
        os.system("python3 botListen.py")
        os.system("python3 interpretAudio.py")
        os.system("python3 interpretInputText.py")
    else:
        botSpeak("Please type your query below")
        print("Please type your query below:")
        query = input()
        with open("userInput.txt", 'w') as uI:
    	    uI.write(query)
        os.system("python3 interpretInputText.py")
else:
    print("Sorry. Most probably you are offline.\nPlease connect to the internet and try again.")