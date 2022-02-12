from word2number import w2n
import inflect
import os

def botSpeak(data):
    with open("botSpeech.txt", 'w') as bS:
        bS.write(data)
    os.system("python3 botSpeak.py")
    os.system("python3 playAudio.py")

def errorcall():
    print("Sorry! That doesn't bring up any result")
    botSpeak("Sorry! That doesn't bring up any result")

def succcesscall(result, operation):
    print("The result of the " + operation + " is " + result)
    botSpeak("The result of the " + operation + " is " + result)



mathFile = open("arithmetic.txt", 'r')
command = mathFile.read()
userText = command.split("##")[0]
code = command.split("##")[1]
numbers = []

for word in userText.split():
    if(word.isdigit()):
        numbers.append(int(word))
        print(numbers)

if(len(numbers) == 0):
    errorcall()

if(code == 'add'):
    if(len(numbers) < 2):
        errorcall()
    else:
        sum = 0
        for number in numbers:
            sum += number
        succcesscall(str(sum), code)

elif(code == 'sub'):
    if(len(numbers) != 2):
        errorcall()
    else:
        diff = numbers[0]-numbers[1]
        succcesscall(str(diff), code)

elif(code == 'mul'):
    if(len(numbers) < 2):
        errorcall()
    else:
        prod = 1
        for number in numbers:
            prod *= number
        succcesscall(str(prod), code)

elif(code == 'div'):
    if(len(numbers) != 2):
        errorcall()
    else:
        n1 = float(numbers[0])
        n2 = float(numbers[1])
        q = n1/n2
        succcesscall(str(q), code)

else:
    errorcall()

    
