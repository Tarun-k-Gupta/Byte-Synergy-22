import botSpeak as bS
import playAudio as pA
import GUI

def botSpeak(data):
    with open("botSpeech.txt", 'w') as file:
        file.write(data)
    bS.botSpeak()
    pA.playAudio()

def errorcall(textBox):
    botSpeak("Sorry! That doesn't bring up any result")
    GUI.guiPrint(textBox, "Sorry! That doesn't bring up any result")
    botSpeak("If you want you can type your query next time")
    GUI.guiPrint(textBox, "If you want you can type your query next time!")
    botSpeak("The numbers you type must be in decimal notation")
    GUI.guiPrint(textBox, "The numbers you type must be in decimal notation")
    botSpeak("Also the operands and operators should be space separated.")
    GUI.guiPrint(textBox, "Also the operands and operators should be space separated.\nFor example: 2<space>+<space>3")
    exit()

def succcesscall(result, operation, textBox):
    botSpeak("The result of the " + operation + " is " + result)
    GUI.guiPrint(textBox, "The result of the " + operation + " is " + result)


def calculate(textBox):
    mathFile = open("arithmetic.txt", 'r')
    command = mathFile.read()
    userText = command.split("##")[0].lower()
    code = command.split("##")[1].lower()
    numbers = []

    for word in userText.split():
        if(word.isdigit()):
            numbers.append(int(word))

    if(len(numbers) == 0):
        errorcall(textBox)

    if(code == 'add'):
        code = 'addition'
        if(len(numbers) < 2):
            errorcall(textBox)
        else:
            sum = 0
            for number in numbers:
                sum += number
            succcesscall(str(sum), code,textBox)

    elif(code == 'sub'):
        code = 'subtraction'
        if(len(numbers) != 2):
            errorcall(textBox)
        else:
            diff = numbers[0]-numbers[1]
            succcesscall(str(diff), code, textBox)

    elif(code == 'mult'):
        code = 'multiplication'
        if(len(numbers) < 2):
            errorcall(textBox)
        else:
            prod = 1
            for number in numbers:
                prod *= number
            succcesscall(str(prod), code, textBox)

    elif(code == 'div'):
        code = 'division'
        if(len(numbers) != 2):
            errorcall(textBox)
        else:
            n1 = float(numbers[0])
            n2 = float(numbers[1])
            q = n1/n2
            succcesscall(str(q), code, textBox)
    elif(code == 'mod'):
        code = 'modulo operation'
        if(len(numbers) != 2):
            errorcall(textBox)
        else:
            n1 = int(numbers[0])
            n2 = int(numbers[1])
            m = n1%n2
            succcesscall(str(m), code, textBox)

    else:
        errorcall(textBox)

    
