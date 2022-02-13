import sys

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
query = sys.argv[1]
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

print("total_cases: " + total_cases + " total_deaths: " + total_deaths + " total_recovered: " + total_recovered + " active_cases: " + active_cases)
driver.quit()
