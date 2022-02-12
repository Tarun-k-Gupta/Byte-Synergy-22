########################CURRENTLY UNDER DEVELOPEMENT#########################
from doctest import master
from itertools import count
from datetime import datetime
from datetime import date
import os
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

    #We can ADD MORE CODE USING elif statements


elif(type == "OPEN"): #Opening native apps
    dummy = 1 #DELETE THIS LINE


elif(type == "SEARCH"): #Web search
    index = -1
    wordList=["for", "about", "regarding"]
    iList=[]
    inputList = inputText.split(" ")
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
        botSpeak("If you want you can type in your query next time")
        print("If you want you can type in your query next time!")
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