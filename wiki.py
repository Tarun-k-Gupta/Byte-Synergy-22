import requests
from gtts import gTTS
import sys
from playsound import playsound
import os
# search_term = str(input("enter search term: "))
search_website = str(input("enter search website: "))
search_query = search_website.lstrip('https://en.wikipedia.org/wiki/')

url = 'https://en.wikipedia.org/w/api.php' + '?format=json&action=query&prop=extracts&explaintext=1&titles=' + search_query
# response = requests.get(
#     'https://en.wikipedia.org/w/api.php',
#     params={
#         'action': 'query',
#         'format': 'json',
#         'titles': search_term,
#         'prop': 'extracts',
#         'exintro': 1,
#         'explaintext': 1,
#     }
# ).json()

response = requests.get(url).json()

page = next(iter(response['query']['pages'].values()))

output = []

try:
    for i in page['extract']:
        output.append(i)
        if i == '\n':
            break
        else:
            continue
except:
    print("Search term could not be found")

string = ""
text_file = open("wiki.txt", "w")
text_file.write(string.join(output))
text_file.close()
myText = ""
with open("wiki.txt", 'r') as s:
    myText = s.read()
myLang = 'en-in'

myAudio = gTTS(text=myText, lang=myLang, slow=False)
os.remove("wiki.txt")
myAudio.save("wiki.wav")
text_file.close()
print(string.join(output))
playsound('wiki.wav')
os.remove("wiki.wav")

