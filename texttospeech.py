from gtts import gTTS
from playsound import playsound

def readFile(fileName):
    f = open(fileName,'r')
    content = f.readlines()
    return content
def TexttoSpeech(message):
    speech = gTTS(text= message)
    speech.save('Test.mp3')
    playsound('Test.mp3')

content = readFile('Podcast1.txt')
TexttoSpeech(content[0])