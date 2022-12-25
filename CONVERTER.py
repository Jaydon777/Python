'''import pyttsx3

text_speech = pyttsx3.init()
ans = input("What do you want to convert?")
text_speech.say(ans)
text_speech.runAndWait()'''

from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
import os
root = Tk()
root.geometry("400x400")
root.configure(bg='grey')
root.title("Text To Speech Converter")
Label(root, text = "Text To Speech", font = "arial 20 bold", bg='white').pack()
Label(text ="Using Google TTS Module", font = 'arial 10 bold italic', bg ='white' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=150,y=80)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=50,y=150)
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Speech.mp3')
    playsound('Speech.mp3')
    Msg.set("")
    os.remove('Speech.mp3')
def Exit():
    root.destroy()
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '10').place(x=50,y=240)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '10' , command = Exit, bg = 'Red').place(x=225 , y = 240)
root.mainloop()