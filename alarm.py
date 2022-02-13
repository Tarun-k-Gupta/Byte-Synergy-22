import time
from gtts import gTTS
import sys
from playsound import playsound
import os
from datetime import datetime
now = datetime.now()
while(True):
    current_time = now.strftime("%H:%M")
    time.sleep(1)
    if sys.argv[1] == current_time:
        print(sys.argv[2])
        text_file = open('alarm.txt', 'w')
        text_file.write(sys.argv[2])

        myText = ""
        with open("alarm.txt", 'r') as s:
            myText = s.read()
        myLang = 'en-in'

        myAudio = gTTS(text=myText, lang=myLang, slow=False)
        os.remove("alarm.txt")
        myAudio.save("alarm.wav")
        text_file.close()
        playsound('alarm.wav')
        os.remove("alarm.wav")
        break
