import pyttsx3
import os

#initilizing the engine
engine = pyttsx3.init()
while True :
    text = input(">")
    #changing the text and saying it
    engine.say(text)
    engine.runAndWait()

    if text == "quit()" :
        break