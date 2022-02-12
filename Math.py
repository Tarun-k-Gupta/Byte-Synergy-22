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

def succcesscall(result, operation):
    botSpeak("The result of the " + operation + " is " + result)


def getNumbers(text):
    p = inflect.engine()
    keyNumbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
                'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 
                'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 
                'hundred', 'thousand', 'lakh', 'crore']


    digits = keyNumbers[0:10]
    multipliers = keyNumbers[28:]

    words = text.split()
    words.append('null')


    grandFinalNumbers = []
    numbers = []

    for word in words:
        if word in keyNumbers:
            numbers.append(word)
        elif (word == 'not'):
            numbers.append('_')
        elif ((word == 'and') and (numbers[len(numbers)-1] in multipliers)):
            numbers.append("+")
        else:
            i = 0
            finalNumbers = []
            while (i < len(numbers)):
                if numbers[i] in keyNumbers:
                    if(len(finalNumbers) != 0):
                        if numbers[i] in multipliers :
                            finalNumbers[len(finalNumbers) - 1] *= w2n.word_to_num(numbers[i])
                            i += 2
                        else:
                            finalNumbers[len(finalNumbers) - 1] += w2n.word_to_num(numbers[i])
                            i += 2
                    else:
                        finalNumbers.append(w2n.word_to_num(numbers[i]))
                        i += 1
                elif (numbers[i] == '_'):
                    if (numbers[i+1] in digits) and (p.number_to_words(finalNumbers[len(finalNumbers) - 1]) in digits):
                        finalNumbers[len(finalNumbers) - 1] = int(str(finalNumbers[len(finalNumbers) - 1]) + '0' + str(w2n.word_to_num(numbers[i+1])))
                    else:
                        return []
                    i += 2
                elif (numbers[i] == '+'):
                    if numbers[i+1] in multipliers:
                        return []
                    else:
                        finalNumbers[len(finalNumbers) - 1] += w2n.word_to_num(numbers[i+1])
                    i += 2
            
            for number in finalNumbers:
                grandFinalNumbers.append(number)
            numbers = []
    
    return grandFinalNumbers

mathFile = open("arithmetic.txt", 'r')
command = mathFile.read()
userText = command.split("##")[0]
code = command.split("##")[1]
numbers = []

numbers = getNumbers(userText)

if(len(numbers) == 0):
    errorcall()

if(code == 'addition'):
    if(len(numbers) < 2):
        errorcall()
    else:
        sum = 0
        for number in numbers:
            sum += number
        succcesscall(str(sum), code)

elif(code == 'subtraction'):
    if(len(numbers) != 2):
        errorcall()
    else:
        diff = numbers[0]-numbers[1]
        succcesscall(str(diff), code)

elif(code == 'multiplication'):
    if(len(numbers) < 2):
        errorcall()
    else:
        prod = 1
        for number in numbers:
            prod *= number
        succcesscall(str(prod), code)

elif(code == 'division'):
    if(len(numbers) != 2):
        errorcall()
    else:
        n1 = float(numbers[0])
        n2 = float(numbers[1])
        q = n1/n2
        succcesscall(str(q), code)

else:
    errorcall()

    
