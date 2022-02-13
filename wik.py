import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Web3"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

try:
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
