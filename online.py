from gtts import gTTS
import os

a = input("What to Convert: ")
b = input("File name: ")
lan = "en"
obj = gTTS(text = a, lang = lan, slow = False)
obj.save(b + ".mp3")
os.system("mpg321 " + b + ".mp3")
