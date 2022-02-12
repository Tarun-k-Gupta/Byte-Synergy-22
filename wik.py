import requests
from bs4 import BeautifulSoup
import re
url = "https://en.wikipedia.org/wiki/Fermat%27s_little_theorem"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

print(soup.find('h1', {"id": "firstHeading"}).text)
firstp = soup.find('p',class_="")
print(firstp.text)

for i in firstp.next_siblings:
    if(i.name == 'p' or i.name == 'h2'):
        if(i.name == 'h2'):
            i = i.text.replace('[edit]','')
            if(i == 'See also' or i == 'Publications'):
                break
            print(i)
            continue
        
        print(i.text)