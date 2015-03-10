import sys
import pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')


for voice in voices:
    if voice.gender == "female":
        engine.setProperty('voice', voice.id)
        break

engine.say(sys.argv[1])

engine.runAndWait()
