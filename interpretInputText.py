########################CURRENTLY UNDER DEVELOPEMENT#########################
from curses.textpad import Textbox
from doctest import master
from itertools import count
from datetime import datetime
import subprocess
from datetime import date
import os
import platform
import time
import botSpeak as bS
import playAudio as pA
import searchEngine as se
import Math as MATH
import GUI
import botListen as bL
import interpretAudio as iA
import tkinter as tk
import scraper as sc
import wiki as wk

def actionDetector(keywords, inputText):
    strictness = 0.85
    count = int(round(strictness*len(keywords)))
    wordHash = {}
    inpLst = inputText.split(" ")
    for word in inpLst:
        wordHash[word.lower()] = 0
    for word in keywords:
        wordHash[word.lower()] = 1
    for word in inpLst:
        if(wordHash[word.lower()] == 1):
            count = count - 1
    if(count <= 0):
        return True
    else:
        return False

def buildKeywords(text): #Extracts important words from the given text
    wordHash = {}
    keywords = []
    textWords = text.split(" ")
    for word in textWords:
        wordHash[word.lower()] = 0

    #Add more useless words which should be removed from the text:
    uselessWords = [["a", "an", "the"], ["alas", "hurray", "bravo", "oh"]]

    #Removing useless words:
    for group in uselessWords:
        for word in group:
            wordHash[word.lower()] = 1
    
    for word in textWords:
        if(wordHash[word.lower()] == 0):
            keywords.append(word.lower())
    return keywords

def botSpeak(data):
    with open("botSpeech.txt", 'w') as file:
        file.write(data)
    bS.botSpeak()
    pA.playAudio()

def findIndex(inputList, word):
    index = -1
    for i in range(len(inputList)):
        if(inputList[i] == word):
            index = i
            break
    return index


def interpretInputText(textBox):


    inputText = ""
    with open("userInput.txt", 'r') as uI:
        inputText = uI.read()
        inputText = inputText.split("\n")[0]
    os.remove("userInput.txt")

    keywords = []
    type = "UNKNOWN"
    reply = "UNKNOWN"
    with open("database", 'r') as db:
        for line in db:
            masterList = line.split("##")
            keywords = masterList[0].split(" ")
            if(actionDetector(keywords, inputText)):
                type = masterList[1]
                reply = masterList[2]
                break

    def teach():
        botSpeak("For teaching me you need to tell me the exact sentence that I should speak!")
        bL.botListen()
        iA.interpretAudio(textBox)
        reply = ""
        with open("userInput.txt", 'r') as uI:
            reply = uI.read()
        os.remove("userInput.txt")
        keywords = buildKeywords(inputText)
        type = "GEN"
        entry = ""
        for word in keywords:
            entry = entry + word + " "
        entry = entry[:-1]
        entry = entry + "##" + type + "##" + reply + "\n"
        with open("database", 'a') as db:
            db.write(entry)

    #Performing the required task based on user input:    
    if(type == "GEN_SPECIFIC"): #Real time actions (eg: finding out time, date etc..)
        topic = reply.split("_")[1].split("\n")[0].lower()
        if(topic == "time"):
            currentTime = time.strftime("%H:%M")
            botSpeak("It is "+currentTime+" right now")
            GUI.guiPrint(textBox, "It is "+currentTime+" right now")

        elif(topic == "day"):
            dayList=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            day = dayList[datetime.today().weekday()]
            botSpeak("Today is "+day)
            GUI.guiPrint(textBox, "Today is "+day)
        
        elif(topic == "month"):
            date = datetime.now()
            month = date.strftime("%B")
            botSpeak("It's "+month)
            GUI.guiPrint(textBox, "It's "+month+"!")

        elif(topic == "year"):
            date = datetime.now()
            year = str(date.today()).split("-")[0]
            botSpeak("The current year is "+str(year))
            GUI.guiPrint(textBox, "The current year is "+str(year))

        elif(topic == "date"):
            date = datetime.now()
            month = date.strftime("%B")
            lst = str(date.today()).split("-")
            day = int(lst[2].split()[0])
            dayStr = str(day)
            if(day == 1):
                dayStr = dayStr + "st"
            elif(day == 2):
                dayStr = dayStr + "nd"
            elif(day == 3):
                dayStr = dayStr + "rd"
            else:
                dayStr = dayStr + "th"
            botSpeak("Today's date is "+dayStr+" "+month+" "+str(lst[0]))
            GUI.guiPrint(textBox, "Today's date is "+dayStr+" "+month+" "+str(lst[0]))

        elif(topic == 'alarm'):
            Time = input("enter the time(HH:MM) :  ")
            message = input("enter reminder message: ")
            os.system("python3 alarm.py Time message &")

        elif(topic == 'joke'):
            os.system("python3 joke.py Dad")
        elif(topic == 'jokeanimal'):
            os.system("python3 joke.py Animal")
        elif(topic == 'jokevalentines'):
            os.system("python3 joke.py Valentines")
        elif(topic == 'jokefamily'):
            os.system("python3 joke.py family")
        elif(topic == 'jokedad'):
            os.system("python3 joke.py Dad")
        elif(topic == 'jokerelationship'):
            os.system("python3 joke.py relationship")
        #We can ADD MORE CODE USING elif statements


    elif(type == "OPEN"): #Opening native apps
        if(platform.system() == 'Linux'):
            topic = reply.split("_")[1].split("\n")[0].lower()
            if(topic == 'chrome'):
                cmd = 'google-chrome'
                subprocess.call(cmd)
            if(topic == 'firefox'):
                cmd = 'firefox'
                subprocess.call(cmd)
            if(topic == 'code'):
                cmd = 'code'
                subprocess.call(cmd)
            if(topic == 'spotify'):
                cmd = 'spotify'
                subprocess.call(cmd)
            if(topic == 'software'):
                cmd = 'gnome-software'
                subprocess.call(cmd)
            if(topic == 'dropbox'):
                cmd = 'dropbox'
                subprocess.call(cmd)
    #Note: -Due to lack of time, and since opening native apps is OS dependent, 
    #       we have left this capability on windows and mac machines as future scope.
    #      -Currently the virtual assistant will detect application opening instructions,
    #       but will not perform any task if the user's operating system is windows or mac.

    elif(type == "SEARCH"): #Web search
        inputList = inputText.split(" ")
        if(any(x in inputList for x in ['Coronavirus', 'coronavirus', 'covid', 'Covid', 'SARS', 'virus'])):

                a_set = set(inputList)
                b_set = set(['India', 'Brazil', 'USA', 'UK', 'Germany', 'France', 'Spain', 'Pakistan', 'Italy', 'World', 'Russia', 'Turkey', 'China', 'Bangladesh', 'Mexico', 'Indonesia', 'Japan', 'Philippines', 'South Africa', 'Iran', 'Sri Lanka', 'Finland', 'Myanmar', 'New Zealand', 'Australia'])

                # check length
                if len(a_set.intersection(b_set)) > 0:
                    text = a_set.intersection(b_set)
                    temp = list(text)
                    final_text = temp[0]
                    sc.webscraper(final_text, textBox)
                else:
                    botSpeak("Sorry I didn't get that")
        else:
            index = -1
            wordList=["for", "about", "regarding"]
            iList=[]
            for word in wordList:
                retVal = findIndex(inputList, word)
                if(retVal != -1):
                    iList.append(retVal)
            if(len(iList) != 0):
                index = iList[0]
                for i in range(len(iList)):
                    if(iList[i] < index):
                        index = iList[i]
            index = index + 1
            topic = ""
            for j in range(index, len(inputList)):
                if(j != len(inputList) - 1):
                    topic = topic + inputList[j] + " "
                else:
                    topic = topic + inputList[j]

            if(len(topic) == 0):
                botSpeak("Sorry. I didn't get that. Please try again")
                GUI.guiPrint(textBox, "Sorry. I didn't get that.\nPlease try again.")
                botSpeak("If you want you can type your query next time")
                GUI.guiPrint(textBox, "If you want you can type your query next time!")
            else:
                with open("search.txt", 'w') as s:
                    s.write(topic)
                se.searchFor()
                os.remove("search.txt")
                wk.wiki_search(textBox)


    elif(type == "MATH"): #Arithmetic operations
        topic = reply.split("_")[1].split("\n")[0].lower()
        mathEntry = inputText+"##"+topic
        with open("arithmetic.txt", 'w') as ar:
            ar.write(mathEntry)
        MATH.calculate(textBox)
        os.remove("arithmetic.txt")



    elif(type == "GEN"): #General chit-chatting
        botSpeak(reply.split("\n")[0])
        GUI.guiPrint(textBox, reply.split("\n")[0])


    else:
        botSpeak("Sorry. I didn't get that.")

        teach_me = tk.Tk()
        teach_me.title("Do you want to teach me?")
        teach_me.geometry("500x500")

        yes_button = tk.Button(teach_me, text= "Yes", command= teach)
        yes_button.pack(side= tk.LEFT, padx= 30)

        no_button = tk.Button(teach_me, text= "No", command= teach_me.destroy)
        no_button.pack(side= tk.RIGHT, padx= 30)

        teach_me.mainloop()
    
