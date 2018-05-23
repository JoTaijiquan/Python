import os
import pygame
from gtts import gTTS
from tempfile import TemporaryFile

#lines = open("Alice.txt").read().splitlines()


#for line in lines:
#    print (line)

lines = open("Alice.txt").read()

tts = gTTS(text=lines, lang='en', fast="true")
filename = "tmp.mp3"
tts.save(filename)
