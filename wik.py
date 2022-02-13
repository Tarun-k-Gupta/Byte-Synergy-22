import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import sys
from playsound import playsound
import os

with open('links.txt', 'r') as r:
    allLinks = r.readlines()    
os.remove("links.txt")
    
count = 0    
wiklink=""
for link in allLinks:
    index = link.find("##TRUE")
    if(index != -1):
        count += 1
        wiklink = link.replace("##TRUE", "")

if(count == 0):
    print(allLinks[0].replace("##FALSE",""))
    

p_str=""
try:
    url = wiklink
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.find('h1', {"id": "firstHeading"}).text)
    getp = soup.find('p',class_="")
    p_str = getp.text
    for i in range(1,51):
        p_str = p_str.replace("["+str(i)+"]","")
    print(p_str)
except:
    pass


def botSpeak(data):
    with open("botSpeech.txt", 'w') as bS:
        bS.write(data)
    os.system("python3 botSpeak.py")
    os.system("python3 playAudio.py")
    
botSpeak(p_str) 
