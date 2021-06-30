import speech_recognition as sr
import pyttsx3
import datetime
import random
from playsound import playsound
import subprocess
import pywhatkit
import wikipedia
import pyjokes


english_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', english_voice)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_to_a_command():
    try:
        with sr.Microphone() as mic:
            print('listening...')
            voice = listener.listen(mic)
            command = listener.recognize_google(voice)
            command=command.lower()           
            #print(command)
    except:
        pass
    return command

def run_command():
    command = listen_to_a_command()
    #print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M: %p')
        #print(time)
        speak('Current time is ' + time ) #aktualna godzina
    
    elif 'date' in command:
        today = datetime.date.today()
        date = today.strftime('%A %d %B %Y')
        #print(date)
        speak("It's" + date) #aktualna data


    elif "tell me about" in command:
        search = command.replace('tell me about', '')
        info = wikipedia.summary(search, 2) 
        #print(info)
        speak(info) # dwa zdania z wiki na dany temat
    
    elif "search for" in command:
        google = command.replace('search for', '')
        google_output = pywhatkit.search(google)
        speak("Searching for "+ google)

    elif 'play' in command:
        video = command.replace('play', '')
        #print(song)
        speak('playing '+ video)
        pywhatkit.playonyt(video) #odpala pierwszy film na yt jaki znajdzie na dany temat
    
    elif 'joke' in command:
        speak(pyjokes.get_joke()) #żarcik
    
    elif 'create a note' in command:
        date = datetime.datetime.now().strftime('%d:%m:%Y %H:%M')
        file_name = str(date).replace(":", "-") + ' note.txt'
        text = command.replace('create a note', '')
        with open(file_name, "w") as f:
            f.write(text) 
        speak("I've created a note") #tworzy notatke
    
    elif 'flip a coin' in command:
        flip = random.randint(0, 1)
        playsound("sounds/CoinToss.wav")
        if (flip == 0):
            speak("It's heads")
        else:
            speak("It's tails")

    elif 'roll a die' in command:
        roll = random.randint(0, 5) + 1
        playsound("sounds/DiceRoll.mp3")
        speak("It's " + str(roll) )

    elif "stop" in command:
        exit()

    else:
        speak("Please repeat that command.") #nie rozumie komendy

while True:
    run_command()