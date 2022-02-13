import random
import time
from gtts import gTTS
import sys
from playsound import playsound
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import lxml
from bs4 import BeautifulSoup


query = sys.argv[1]
if(query == 'Animal'):
    page = 'https://www.rd.com/jokes/animal/'
    n = random.randint(1, 70)
elif(query == 'Valentines'):
    page = 'https://www.rd.com/jokes/valentines-day-jokes/'
    n = random.randint(1, 70)
elif(query == 'Dad'):
    page = 'https://www.rd.com/jokes/dad/'
    n = random.randint(1, 70)
elif(query == 'relationship'):
    page = 'https://www.rd.com/jokes/relationship/'
    n = random.randint(1, 60)
elif(query == 'family'):
    page = 'https://www.rd.com/jokes/family/'
    n = random.randint(1, 70)

options = Options()
service = Service("./chromedriver")
options.headless = True
driver = webdriver.Chrome(service=service, options=options)
driver.get(page)

list = driver.find_elements(By.XPATH, "//div[@class = 'excerpt-wrapper']")

output = list[n].text
text_file = open("joke.txt", 'w')
text_file.write(output)
text_file.close()
myText = ""
with open("joke.txt", 'r') as s:
    myText = s.read()
myLang = 'en-in'

myAudio = gTTS(text=myText, lang=myLang, slow=False)
os.remove("joke.txt")
myAudio.save("joke.wav")
text_file.close()
print(output)
playsound('joke.wav')
os.remove("joke.wav")
