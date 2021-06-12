import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random

listener = sr.Recognizer()
engine= pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
          #with sr.Microphone() as source:

              #voice= listener.listen(source)
              talk("What can I do for you Sir?")
              command=input("What can I do for you Sir?")
              command= command.lower()

              if 'alexa' in  command:
                command=command.replace('alexa','')
                print(command)
    except:
        talk("Sorry your Mic not be working")
    return command

def run_alexa():
    talk("Hey welcome, I am Jarvis your personal Assistant. ")
    print("Hey welcome, I am Jarvis your personal Assistant ")



    talk("My commands are")
    print(("My Commands are"))

    talk("play song name i will play that song for you")
    print("play song name i will play that song for you")

    talk("Want to know about any famous personality? Dont worry im there write who the hell is that person 's name ")
    print("Want to know about any famous personality? Dont worry im there write who the hell is that person 's name ")

    talk("Forget your watch? Ask me the time ")
    print("Forget your watch? Ask me the time ")

    talk("Worrying nobody gives you a compliment? You can ask that from me")
    print("Worrying nobody gives you a compliment? You can ask that from me")

    talk("Want to know about my master? then ask meh")
    print("Want to know about my master? then ask meh")

    talk("Wanna impress your crush? I can say both jokes and dadjokes")
    print("Wanna impress your crush? I can say both jokes and dadjokes")



    command=take_command()

    print(command)
    if 'play' in command:
        song= command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M %p')
        talk('Current Time is' + time)
        print('Current Time is' + time)

    elif 'who the hell is' in command:
        person=command.replace('who the hell is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('Have you ever seen your face?')
        print('Have you ever seen your face?')

    elif 'intelligent' in command:
        talk('My master Bodhiswattwa is the most intelligent person')
        print('My master Bodhiswattwais the most intelligent person')

    elif 'compliment' in command:
        compli=['You are the most intelligent person','You are dashing','You are very kind and generous','You are a geneuis','you are handsome']
        play=random.choice(compli)
        talk(play)
        print(play)

    elif 'god of death' in command:
        talk('Not Today')
        print('Not Today')

    elif 'master' in command:
        talk('Bodhiswattwa of House Chakraborty, King of The Andals And the first man, Protector of The Realm and Lord of the Seven Kingdoms')

        print('Bodhiswattwa of House Chakraborty, King of The Andals And the first man, Protector of The Realm and Lord of the Seven Kingdoms')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'dad joke' in command:
        lis=['Dad, did you get a haircut?" "No, I got them all cut!','My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!','I dont trust stairs. They re always up to something.','What do you call someone with no body and no nose? Nobody knows.','What time did the man go to the dentist? Tooth hurt-y.','This graveyard looks overcrowded. People must be dying to get in.','What concert costs just 45 cents? 50 Cent featuring Nickelback!','What kind of shoes do ninjas wear? Sneakers!','How does a penguin build its house? Igloos it together.','Im on a seafood diet. I see food and I eat it.']
        player=random.choice(lis)
        talk(player)
        print(player)

    else:
        talk("Please say the again")
        print("Please say the again")


while True:
    run_alexa()




