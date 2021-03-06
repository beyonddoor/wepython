from datetime import datetime   
from playsound import playsound

import pyttsx3

def read_pdf(file):
    import PyFDF2

    speaker = pyttsx3.init()
    pdfreader = PyFDF2.PdfFileReader(open(file, 'rb'))

    for page_num in range(pdfreader.numPages):
        text= pdfreader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()
        
    speaker.stop()

def read_text(filename):
    speaker = pyttsx3.init()
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line)
        speaker.say(line)
        speaker.runAndWait()
    speaker.stop()

read_text('bin/chs.txt')

