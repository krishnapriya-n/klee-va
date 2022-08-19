###### AI Assistant Klee ######
# Klee listens to the commands given by the user and executes
#  certain functions. Klee is mainly a conversation-based bot who
# talks to the user enthusiastically.

#### Character Klee is owned by Genshin Impact Game by Hoyoverse.
#### Author: Krishna Priya Nimmagadda
#### Started: June 2022

## IMPORTS ##
"These imports are for various module that will be used throught this code."

# Speech recognition module is for voice listening.
import speech_recognition as sr 
# Datetime is for wishing the user at different times of the day.
import datetime
# OS Module is for the operating system.
import os
# Playsound plays the voicelines of Character Klee.
from playsound import playsound
# Random module plays random voice lines. This is used in hello function.
import random

class Klee:
    'Class Klee contains all the defined functions for playing the'
    'prompted various voicelines'

    ## INTRODUCE FUNCTION ##
    "Introduce function is played when user prompts by saying statements"
    "such as 'who are you' or 'what are you' (ending -are you)"

    def introduce():
        playsound ('C:/Users/lenovo/Desktop/Klee VA/Voices/Klee_Hello.mp3')

    ## HELLO FUNCTION ##
    "Hello function is played when user prompts by saying statements"
    "such as 'hello'. Here there are four voice files that are played"
    "randomly. We use the random module here."

    def hello():
        path = 'C:/Users/lenovo/Desktop/Klee VA/Voices/Hellos/'
        files = os.listdir(path)
        try:
            rand = random.choice(files)
            playsound('C:/Users/lenovo/Desktop/Klee VA/Voices/Hellos/' + rand)
        
        except Exception as e:
            print(e)

    ## FRIEND FUNCTION ##
    "Friend function is played when user prompts by saying statements"
    "such as 'who is your friend' (contains 'friend' in statement)"

    def friend():
        playsound ('C:/Users/lenovo/Desktop/Klee VA/Voices/Klee_Friend.mp3')

    ## BIRTHDAY FUNCTION ##
    "Birthday function is played when user prompts by saying statements"
    "such as 'It's my birthday' (contains 'birthday' in statement)"

    def birthday():
        playsound ('C:/Users/lenovo/Desktop/Klee VA/Voices/Klee_Birthday.mp3')

    ## HOBBIES FUNCTION ##
    5

    def hobbies():
        playsound ('C:/Users/lenovo/Desktop/Klee VA/Voices/Klee_Hobbies.mp3')

    ## ACTIVITIES FUNCTION ##
    def today():
        playsound ('C:/Users/lenovo/Desktop/Klee VA/Voices/Klee_Spoils.mp3')

    ## WISHING THE USER FUNCTION ##
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            playsound ('C:/Users/lenovo/Desktop/Klee VA/Voices/Klee_Morning.mp3')
        elif hour >= 12 and hour < 15:
            playsound ('C:/Users/lenovo/Desktop/Klee VA/Voices/Klee_Afternoon.mp3')
        elif hour >= 15 and hour < 19:
            playsound ('C:/Users/lenovo/Desktop/Klee VA/Voices/Klee_Evening.mp3')
        else:
            playsound ('C:/Users/lenovo/Desktop/Klee VA/Voices/Klee_Night.mp3')

    ## INPUT FROM MICROPHONE ##   
    """It takes microphone input from the user and returns string output"""
 
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("I didn't get you. Please repeat...")  
            return "None"
        return query

if __name__ == "__main__":
    while True:
        query = Klee.takeCommand().lower()

        if 'hello' in query or 'klee' in query or 'hi' in query:
            Klee.hello()

        elif 'who are you' in query or 'your name' in query:
            Klee.introduce()
    
        elif 'good' in query:
            Klee.wishMe()

        elif 'friend' in query:
            Klee.friend()

        elif 'birthday' in query:
            Klee.birthday()

        elif 'like' in query:
            Klee.hobbies()

        elif 'did you do'in query:
            Klee.today()

        elif 'thank you' in query:
            quit()
