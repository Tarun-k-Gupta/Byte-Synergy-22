import tkinter as tk
from tkinter import *
import urllib.request
import time
import botSpeak as bS
import playAudio as pA
import botListen as bL
import interpretAudio as iA
import interpretInputText as iIT


def func():
    print("l")

def mic_func():
    new_mic_window = tk.Tk()
    new_mic_window.title("Microphone")
    new_mic_window.geometry("500x500")
    
    T = Text(new_mic_window)
    bL.botListen()
    iA.interpretAudio(T)
    iIT.interpretInputText(T)
    new_mic_window.mainloop()

def kbd_func():
    def internal():
        userText= T.get(1.0, "end-1c")
        with open("userInput.txt", 'w') as file:
            file.write(userText)
        iIT.interpretInputText(T)
        T.insert(END, "Click on NEXT for your next command\n")

    def clear():
        T.delete(1.0, "end")

    new_kbd_window = tk.Tk()
    new_kbd_window.title("KeyBoard")
    new_kbd_window.geometry("500x500")

    T = Text(new_kbd_window)
    T.pack()

    ok_btn = Button(new_kbd_window, height= 2, width= 50, text= "OK", command= internal)
    ok_btn.pack()

    clear_btn = Button(new_kbd_window, height= 2, width= 50, text= "NEXT", command= clear)
    clear_btn.pack()

    new_kbd_window.mainloop()

def greetText():
    currentTime = time.strftime("%H:%M:%S")
    lst=currentTime.split(":")
    totMins = int(lst[0])*60 + int(lst[1])
    greetText = ""
    if (totMins >= 300 and totMins <= 719):
        greetText = "Good Morning"
    elif (totMins >= 720 and totMins <= 1019):
        greetText = "Good Afternoon"
    else:
        greetText = "Good Evening"
    return greetText

def botSpeak(data):
    with open("botSpeech.txt", 'w') as file:
        file.write(data)
    bS.botSpeak()
    pA.playAudio()


def guiPrint(T, text):
    T.insert(tk.END, '\n'+text+'\n')
    T.pack()


def zara_window():
    zara = tk.Tk()
    zara.title('Zara')
    zara.geometry("1500x1500")

    mic = PhotoImage(file= "images/mic.png")
    mic_button = tk.Button(zara,image= mic, height= 150, width= 150, command= mic_func)
    mic_button["border"] = 0
    mic_button.pack(side= LEFT, padx= 310)

    kbd = PhotoImage(file= "images/kbd.png")
    kbd_button = tk.Button(zara, image= kbd, height= 150, width= 150, command= kbd_func)
    kbd_button["border"] = 0
    kbd_button.pack(side= RIGHT, padx= 310)

    zara_img = PhotoImage(file= "images/zara.png")
    Label(zara, image= zara_img, height= 150, width= 300).pack(pady= 350)

    T = Text(zara)
    guiPrint(T, greetText())
    botSpeak(greetText())

    zara.mainloop()


def isOnline():
    url= "http://google.com"

    try:
        req = urllib.request.urlopen(url)
        return True
    except:
        return False


def run():
    if(isOnline()):
        zara_window()
    else:
        error_win = tk.Tk()
        error_win.title("Error!")
        error_win.geometry("500x500")

        T = Text(error_win)
        guiPrint(T, "You are offline!")
        guiPrint(T, "Try Again")
        #T.insert(tk.END, " You are offline!")
        #T.pack(pady= 20)

        error_win.mainloop()

