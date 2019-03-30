import speech_recognition as sr
import os
import pyttsx3
import sys,webbrowser
import requests, json
import smtplib

s=sr.Recognizer()
with sr.Microphone() as Source:
    p='Please speak what u want to do'
    print(p)
    engine = pyttsx3.init()
    engine.say(p)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    print('1- Google\n2- Mail\n3- Weather\n4- Map\n5- Youtube')
    a=s.listen(Source)
    print(a)

data=s.recognize_google(a)
print(data)

#Code for searching on google
if(data=='Google'):
    with sr.Microphone() as Source:
        p1='What are u looking for sir?'
        print(p1)
        engine = pyttsx3.init()
        engine.say(p1)
        engine.setProperty('volume',1.0)
        engine.runAndWait()
        s1=s.listen(Source)
        print(s1)

    data1=s.recognize_google(s1)
    print(data1)
    webbrowser.open("https://google.com/search?q=%s" % data1)

    engine = pyttsx3.init()
    engine.say(data1)
    engine.setProperty('volume',1.0)
    engine.runAndWait()

#Code for weather report
if(data=='weather'):
    with sr.Microphone() as Source:
        p2='Of which city sir?'
        print(p2)
        engine = pyttsx3.init()
        engine.say(p2)
        engine.setProperty('volume',1.0)
        engine.runAndWait()
        s2=s.listen(Source)
        print(s2)

    city_name=s.recognize_google(s2)
    print(city_name)
    
    api_key = "1974045ec5c3228223bc7759818dbc14"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 

    engine = pyttsx3.init()
    engine.say('Here\'s the weather sir')
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description)) 

    else: 
            print(" City Not Found ")


#Code for Map--
if(data=='map'):
    t='Of which location sir?'
    print(t)
    engine = pyttsx3.init()
    engine.say(t)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    with sr.Microphone() as Source:
        s3=s.listen(Source)
        location=s.recognize_google(s3)
        print(location)
        webbrowser.open('https://www.google.com/maps/place/'+location)

#Code for Mail--

if(data=='mail'):
    with sr.Microphone() as Source:
            r_email=input('Please enter receiver\'s email address\n')
            engine = pyttsx3.init()
            engine.say(r_email)
            engine.setProperty('volume',1.0)
            engine.runAndWait()
            p1='What do you want to send, sir?'
            print(p1)
            engine = pyttsx3.init()
            engine.say(p1)
            engine.setProperty('volume',1.0)
            engine.runAndWait()
            s4=s.listen(Source)
            print(s4)
            content=s.recognize_google(s4)
            print(content)

    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("ankit02111997@gmail.com","Ankitkk1$")
    mail.sendmail("ankit02111997@gmail.com",r_email,content)
    mail.close()
    print("completed")


    
