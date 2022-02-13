from cmath import inf
from word2number import w2n
import inflect


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

def link(link):
    words = link.split('/')
    print(words)

link("https://en.wikipedia.org/wiki/Luther_(TV_series)")