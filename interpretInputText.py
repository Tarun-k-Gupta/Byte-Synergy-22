########################CURRENTLY UNDER DEVELOPEMENT#########################
from doctest import master
from itertools import count
from datetime import datetime
import subprocess
from datetime import date
import os
import platform
import time
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
    with open("botSpeech.txt", 'w') as bS:
        bS.write(data)
    os.system("python3 botSpeak.py")
    os.system("python3 playAudio.py")

def findIndex(inputList, word):
    index = -1
    for i in range(len(inputList)):
        if(inputList[i] == word):
            index = i
            break
    return index




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

#Performing the required task based on user input:    
if(type == "GEN_SPECIFIC"): #Real time actions (eg: finding out time, date etc..)
    topic = reply.split("_")[1].split("\n")[0].lower()
    if(topic == "time"):
        currentTime = time.strftime("%H:%M")
        botSpeak("It is "+currentTime+" right now")
        print("It is "+currentTime+" right now")

    elif(topic == "day"):
        dayList=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = dayList[datetime.today().weekday()]
        botSpeak("Today is "+day)
        print("Today is "+day)
    
    elif(topic == "month"):
        date = datetime.now()
        month = date.strftime("%B")
        botSpeak("It's "+month)
        print("It's "+month+"!")

    elif(topic == "year"):
        date = datetime.now()
        year = str(date.today()).split("-")[0]
        botSpeak("The current year is "+str(year))
        print("The current year is "+str(year))

    elif(topic == "date"):
        date = datetime.now()
        month = date.strftime("%B")
        lst = str(date.today()).split("-")
        day = int(lst[2])
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
        print("Today's date is "+dayStr+" "+month+" "+str(lst[0]))

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
    if(any(x in inputList for x in ['Coronavirus', 'coronavirus', 'covid', 'Covid', 'SARS'])):

            a_set = set(inputList)
            b_set = set(['India', 'Brazil', 'USA', 'UK', 'Germany', 'France', 'Spain', 'Pakistan', 'Italy'])

            # check length
            if len(a_set.intersection(b_set)) > 0:
                text = a_set.intersection(b_set)
                temp = list(text)
                final_text = temp[0]
                print(final_text)
                os.system("python3 scraper.py final_text")
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
            print("Sorry. I didn't get that.\nPlease try again.")
            botSpeak("If you want you can type your query next time")
            print("If you want you can type your query next time!")
        else:
            with open("search.txt", 'w') as s:
                s.write(topic)
            os.system("python3 searchEngine.py")
            os.remove("search.txt")


elif(type == "MATH"): #Arithmetic operations
    topic = reply.split("_")[1].split("\n")[0].lower()
    mathEntry = inputText+"##"+topic
    with open("arithmetic.txt", 'w') as ar:
        ar.write(mathEntry)
    os.system("python3 Math.py")
    os.remove("arithmetic.txt")



elif(type == "GEN"): #General chit-chatting
    botSpeak(reply.split("\n")[0])
    print(reply.split("\n")[0])


else:
    botSpeak("Sorry. I didn't get that.")
    print("Sorry. I didn't get that...")
    botSpeak("Please teach me the reply that I should give for this question.")
    print("Please teach me the reply that I should give for this question.")
    botSpeak("For teaching me you need to tell me the exact sentence that I should speak!")
    print("For teaching me you need to tell me the exact sentence that I should speak!")
    os.system("python3 botListen.py")
    os.system("python3 interpretAudio.py")
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