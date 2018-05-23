#Python3.6 + Pygame
# -*- coding: utf-8 -*-

import os
from gtts import gTTS

#tts = gTTS(text="hello", lang='en')
os.system ("echo 'hello world'")
os.system ("say 'hello khem and kram, how are you to day. Is it fun at the dojo?'")

"""
#For PC
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("This is the pc voice speaking")

#For Linux
from espeak import espeak
espeak.synth("Hello world.")
"""