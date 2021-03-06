import requests
import webbrowser
from gtts import gTTS
from playsound import playsound
import os
import multiprocessing


import GUI


def wiki_search(textbox):
    with open('links.txt', 'r') as r:
        allLinks = r.readlines()
    os.remove("links.txt")

    count = 0
    wiklink = ""
    for link in allLinks:
        index = link.find("##TRUE")
        if (index != -1):
            count = count + 1
            wiklink = link.replace("##TRUE", "")
            GUI.guiPrint(textbox, wiklink)
            search_query = wiklink.lstrip('https://en.wikipedia.org/wiki/')
            search = search_query.replace("_", " ")
            search = search.replace("\n", "")
            break

    if (count == 0):
        string = allLinks[0].replace("##FALSE", "")
        GUI.guiPrint(textbox, string)
        webbrowser.open_new(string)
        exit()

    response = requests.get(
        'https://en.wikipedia.org/w/api.php',
        params={
            'action': 'query',
            'format': 'json',
            'titles': search,
            'prop': 'extracts',
            'exintro': 1,
            'explaintext': 1,
        }
    ).json()

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
        exit()

    string = ""
    text_file = open("wiki.txt", "w")
    text_file.write(string.join(output))
    text_file.close()
    myText = ""
    with open("wiki.txt", 'r') as s:
        myText = s.read()
    myLang = 'en-in'
    GUI.guiPrint(textbox, myText)
    myAudio = gTTS(text=myText, lang=myLang, slow=False)
    text_file.close()
    os.remove("wiki.txt")
    myAudio.save("wiki.wav")
    print(string.join(output))
    p = multiprocessing.Process(target=playsound, args=("wiki.wav",))
    p.start()
    input()
    p.terminate()
    os.remove("wiki.wav")

