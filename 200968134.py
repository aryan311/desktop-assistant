from http import server

import pyautogui
import pyttsx3 #text data to speech

import datetime #to read and write date and time

import speech_recognition as sr
#it converts mic input to text
import smtplib #for email sending purpose

from secret import senderEmail, pwd, to 
#here I've created a secret.py file to store my login credentials for email purpose and in pwd we need to do enter a password taken from gmail.with app acess
from email.message import EmailMessage

import pyaudio
import webbrowser as wb #because we will be using wathsaap web
from time import sleep #using this fuction we cam stop a program for a specific time
import wikipedia #to search on wikipedia through voice commands
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard #to read selected text 
import os
import pyjokes #for jokes function
import string
import random
import psutil #to get updates about system
from nltk.tokenize import word_tokenize


engine = pyttsx3.init()
def speak(audio):
    engine.say(audio) #we can any text insidde this barcket wwhich we want our assistant to speak
    engine.runAndWait()
    
def getvoices(voice):
    voices = engine.getProperty('voices') 
    #print(voices[0].id)
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        speak("hello this is Aryan's assistant , I hope your are doing good")
        
    if voice == 2:
        engine.setProperty('voice',voices[1].id) 
        speak("hello this is Aryan's assistant , I hope your are doing good")
        
    
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #strftimne is usesd to define the format in which we want to obtain the date time, I is for hour M for minute and S for second
    speak("The current time is")
    speak(Time) 
    
def date():
    year = int(datetime.datetime.now().year) 
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is :")
    speak(date)
    speak(month)
    speak(year)

def greeting(): 
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour <24:
        speak("Good evening sir!")
    else:
        speak("Good night Sir!")

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    greeting()
#while True:
    #voice = int(input("Enter 1 for male voice and 2 for female\n"))
     #speak(audio)
    #getvoices(voice)
  #time()

#date()
#wishme()  

def takeCommandCMD():
    query = input("Please tell me how can I help You")
    return query

def  takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:# it opens mic and stores input as source
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-IN") #code for language
        #search for google speech recognition language code to get odes for differnet languages
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def send_email(receiver,subject,content):
    server = smtplib.SMTP('smtp.gmail.com', 587) #first we set gmail.com to variable server then we did that id
    server.starttls() # to make it secure
    server.login(senderEmail, pwd) #creating different file for security reason
    # server.sendmail(senderEmail, to, 'content')
    email = EmailMessage()
    email['From']= senderEmail
    email['to']= receiver
    email['subject']= subject
    email.set_content(content)
    server.send_message(email)
    server.close()
    
def sendwhatsaapmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsaap.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')
    #here it will load the whatsaap web and ask for phone number and message and upon prseeing enter key it will send
    
def searchgoogle():
    speak("What should I search for you?")
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

#http://api.openweathermap.org/data/2.5/weather?q={Patna}&units=imperial&appid={a239f20ec0f767ef2853eafc55e7c22d}


def news():
   
    newsapi = NewsApiClient(api_key = '34d2a995dc7a41fa8638faed83d97834')
    speak('What topic you need the news about')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q='topic',
                                     language = 'en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("thats it for now, i will updateyou in sometime")
    
    
def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    
    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths :{data["deaths"]}  \n Recovered{data["recovered"]}'
    
    print(covid_data)
    speak(covid_data)
    
    
def text2speech():
    text= clipboard.paste()
    print(text)
    speak(text)
    
    
def screenshot():
    name_img = (datetime.datetime.now())
    name_img = 'C:\\Users\\aryan\\OneDrive\\Desktop\\AI Assitant\\screenshot\\ss.png'
    img = pyautogui.screenshot(name_img)
    img.show()
    
def password_gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    newpass = ("".join(s[0:passlen])) #password of length 8
    print(newpass)
    speak(newpass)
    
    
def flip():
    speak("Okay sir, flipping a coin")
    coin = ['head','tails'] #adding outputs
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    #it will shuffle the list randomly and give us output 
    speak("i flipped the coin and got"+toss) 
    
    
def roll():
    speak("okay, rolling a dice for you")
    die =  ['1','2','3','4','5','6']# adding all possible outputs
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("I rolled a dice and you got"+roll)
    
def cpu():
    usage =str(psutil.cpu_percent())
    speak('CPU usage is at'+usage)
    battery = psutil.sensors_battery()
    speak('battery percentage is ')
    speak(battery.percent)
    #Gpu = psutil.sensors_gpu
    #speak(Gpu)
    
    
if __name__ == "__main__": #way to call maibn function
    getvoices(2) # here we can set the voice value as 0 or 1 to switch between male and female voices
    wishme()
    wakeword = "assistant" #if we use word assistant in our voice command the only it will give output
    while True:
        #query = takeCommandCMD().lower()
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        print(query)
        if wakeword in query: 
            if 'time' in query:
                time()
            elif 'date' in query:
                date()
            
            
            elif 'email' in query:
                email_list = {
                    'test':'aryankumar94310@outlook.com'# need to add all the emails here to whom so ever we want to send the email
                }
                try:
                    speak("To whom you want to send the mail")
                    name = takeCommandMic()
                    receiver = email_list[name]
                    speak("what is the subject of mail")
                    subject = takeCommandMic()
                    speak('what should I text')
                    content = takeCommandMic()
                    send_email(receiver,subject,content)
                    speak("your email has been send sucessfully")
                except Exception as e:
                    print(e)
                    speak("unable to send the email sucessfully")
                    
            elif 'message' in query:
                user_name = {
                    'Test' : '+91 83407 91938' # add the numbers like this to send the message
                }
                try:
                    speak("To whom you want to send the Whatsaap message")
                    name = takeCommandMic()
                    phone_no = user_name[name]
                    speak("what is the message")
                    message = takeCommandMic()
                    sendwhatsaapmsg(phone_no,message)
                    speak("your message has been send sucessfully")
                except Exception as e:
                    print(e)
                    speak("unable to send the message sucessfully")
            
            
            elif 'wikipedia' in query:
                speak('searching on wikipedia...')
                query = query.replace("wikipedia", "")
                #to remove the word wikipedia from the topic to be searched
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak(result)
                
            elif 'search' in query:
                searchgoogle()
                
            elif 'youtube' in query:
                speak('What should I search for?')
                topic = takeCommandMic()
                pywhatkit.playonyt(topic)
                
            elif 'weather' in query:
                url = f'http://api.openweathermap.org/data/2.5/weather?q=bangalore&units=imperial&appid=a239f20ec0f767ef2853eafc55e7c22d'
                
                res = requests.get(url)
                data = res.json() #data from link is in json format
                
                weather = data['weather'] [0] ['main']
                temp = data['main']['temp']
                des = data['weather'] [0] ['description']
                temp = round((temp - 32) * 5/9) #round off the value
                print(weather)
                print(temp)
                print(des)
                speak(f'weather in ()city is like')
                speak('Temperature : {} degree celcius'.format(temp))
                speak('weather is {}'.format(des))
                
                
            elif 'news' in query:
                news()
                
                
            elif 'read' in query:
                text2speech()
                
                
            elif 'covid' in query:
                covid()
                
            elif 'open  v s code' in query:
                codepath = 'C:\\Users\\aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(codepath)
                
                
            elif 'joke' in query:
                speak(pyjokes.get_joke())
                
            elif 'screenshot' in query:
                screenshot()
                
                
            elif 'remember' in query:
                speak("What should I remember?")
                data = takeCommandMic()
                speak("you said me to remember that"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
                
            elif 'do you remember anything' in query:
                remember = open('data.txt','r')
                speak("you told me to remember that"+remember.read())
                
                
            elif 'generate password' in query:
                password_gen()
                
            elif 'flip' in query:
                flip()
                
            elif 'roll' in query:
                roll()
                
            elif 'system' in query:
                cpu()
                
            elif 'offline' in query:
                speak("going offline, bye")
                quit()  
                
                
#here we can see that for voice inputs nltk library and specially word tokenizer is used so that each word is focused properly and based on those inputs 
# we are able to do some operation properly here some feature are there which will work on every pc which are mentioned below
# wikipedia, search on google, finding youtube videos,  giving covid updates, generating a password , rolling a dice, tossing a coin
# giving system info
# while some require id password like sending email and whatsaap messages 
# some fuctions that can be tried aare:
# assistant search on google
# assistant any topic on wikipedia
# assistant send an email, etc 
            
            
        
         




      

   

