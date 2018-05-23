#Python3.6 + Pygame
# -*- coding: utf-8 -*-

import os
import pygame
from gtts import gTTS
from tempfile import TemporaryFile


tts = gTTS(text="Hello world", lang='en')
filename = "tmp.mp3"
tts.save(filename)

pygame.mixer.init()
pygame.mixer.music.load("tmp.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy()==True:
    continue

os.remove(filename)