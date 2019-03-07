import speech_recognition as sr 
import os
import sys
import webbrowser

def talk(words):
    print(words)
    os.system("say " + words)

talk("Hello ask me anything?")