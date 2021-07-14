import webbrowser
import smtplib
import pyttsx3
import pywhatkit






def open_web(url):
    open(webbrowser.open_new(url))
    pyttsx3.speak('Thank you regards david')


def send_mail_gmail(sender, reciever,message,password):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.login(sender,password)
    server.sendmail(sender,reciever,message)
    pyttsx3.speak('Thank you regards david')

def from_num_to_num(starting_num,End_num):
    for i in range(starting_num,End_num+1):
        print(i)

def speak(text):
    pyttsx3.speak(text)

def open_whatsapp_web():
    pywhatkit.open_web()
