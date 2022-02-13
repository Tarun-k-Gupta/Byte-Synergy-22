import time
from gtts import gTTS
import sys
from playsound import playsound
import os
import GUI
import requests
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

def webscraper(query, textbox):
    page ='https://www.worldometers.info/coronavirus/'
    options = Options()
    service = Service("./chromedriver")
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(page)


    list = driver.find_elements(By.XPATH, "//a[text() = '" +query+ "']/parent::*/parent::*/td[position() = 3 or position() = 5 or position() = 7 or position() = 9]")
    total_cases = str(list[0].text)
    total_deaths = str(list[1].text)
    total_recovered = str(list[2].text)
    active_cases = str(list[3].text)


    output_string = "The total number of cases in " + query + " are " + total_cases + " the total number of deaths are " + total_deaths + " the total number of recovered cases are " + total_recovered + " and the number of active cases are " + active_cases
    GUI.guiPrint(textbox, output_string)
    text_file = open("coronavirus.txt", 'w')
    text_file.write(output_string)
    text_file.close()
    myText = ""
    with open("coronavirus.txt", 'r') as s:
        myText = s.read()
    myLang = 'en-in'

    myAudio = gTTS(text=myText, lang=myLang, slow=False)
    os.remove("coronavirus.txt")
    myAudio.save("coronavirus.wav")
    text_file.close()
    playsound('coronavirus.wav')
    os.remove("coronavirus.wav")
    driver.quit()
    return
