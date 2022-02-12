from word2number import w2n
import inflect
import os

def botSpeak(data):
    with open("botSpeech.txt", 'w') as bS:
        bS.write(data)
    os.system("python3 botSpeak.py")
    os.system("python3 playAudio.py")

def errorcall():
    botSpeak("Sorry! That doesn't bring up any result")
    print("Sorry! That doesn't bring up any result")
    botSpeak("If you want you can type your query next time")
    print("If you want you can type your query next time!")
    botSpeak("The numbers you type must be in decimal notation")
    print("The numbers you type must be in decimal notation")
    botSpeak("Also the operands and operators should be space separated.")
    print("Also the operands and operators should be space separated.\nFor example: 2<space>+<space>3")
    exit()

def succcesscall(result, operation):
    botSpeak("The result of the " + operation + " is " + result)
    print("The result of the " + operation + " is " + result)



mathFile = open("arithmetic.txt", 'r')
command = mathFile.read()
userText = command.split("##")[0].lower()
code = command.split("##")[1].lower()
numbers = []

for word in userText.split():
    if(word.isdigit()):
        numbers.append(int(word))

if(len(numbers) == 0):
    errorcall()

if(code == 'add'):
    code = 'addition'
    if(len(numbers) < 2):
        errorcall()
    else:
        sum = 0
        for number in numbers:
            sum += number
        succcesscall(str(sum), code)

elif(code == 'sub'):
    code = 'subtraction'
    if(len(numbers) != 2):
        errorcall()
    else:
        diff = numbers[0]-numbers[1]
        succcesscall(str(diff), code)

elif(code == 'mult'):
    code = 'multiplication'
    if(len(numbers) < 2):
        errorcall()
    else:
        prod = 1
        for number in numbers:
            prod *= number
        succcesscall(str(prod), code)

elif(code == 'div'):
    code = 'division'
    if(len(numbers) != 2):
        errorcall()
    else:
        n1 = float(numbers[0])
        n2 = float(numbers[1])
        q = n1/n2
        succcesscall(str(q), code)
elif(code == 'mod'):
    code = 'modulo operation'
    if(len(numbers) != 2):
        errorcall()
    else:
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        m = n1%n2
        succcesscall(str(m), code)

else:
    errorcall()

    
