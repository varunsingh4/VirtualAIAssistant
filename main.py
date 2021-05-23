import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")
    elif hour>=12 and hour<18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")
def run_alexa():
    command = take_command()
    wishMe()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk("sorry, I have a boyfriend!")
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'assistant' in command:
        talk('I am Varun Personal Assistant')
    elif 'exit'  in command:
        # The fucntion greets the User GoodBye
        talk("Thank you for Using Varun's AI Assistant.")
        talk("Hope u Had a good experience using AI Assistant!")
        print("Thank You!")
        quit()
    elif 'shutdown' in command:
        os.system("shutdown /r/t 1")
    elif 'search' in command:
        command =command.replace("search","")
        webbrowser.open_new_tab(command)
    else:
        talk('please say the command again')
while True:
    wishMe()
    run_alexa()