import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import sys
from playsound import playsound
import os

with open('links.txt', 'r') as r:
    allLinks = r.readlines()    
    
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
    #printing the main heading
    print(soup.find('h1', {"id": "firstHeading"}).text)

    #getting the first para below the main heading
    getp = soup.find('p',class_="")
    p_str = getp.text
    for i in range(1,51):
        p_str = p_str.replace("["+str(i)+"]","")
    print(p_str)
except:
    pass


string = ""
try:
    text_file.write(p_str)
    text_file = open("wiki.txt", "w")
    text_file.close()
    myText = ""
    with open("wiki.txt", 'r') as s:
        myText = s.read()
    myLang = 'en-in'

    myAudio = gTTS(text=myText, lang=myLang, slow=False)
    os.remove("wiki.txt")
    myAudio.save("wiki.wav")
    text_file.close()
    playsound('wiki.wav')
    os.remove("wiki.wav")
except:
    pass
