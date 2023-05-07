import json
import pyfiglet
import requests
import os
from dotenv import load_dotenv

load_dotenv()

with open('config.json') as config:
    config = json.load(config)

if config['ENV'] == True :
    cookies = os.getenv("ROBLOSECURITY")
else :
    cookies = config['cookie']

def LoginAs():
    session = requests.Session()
    session.cookies['.ROBLOSECURITY'] = cookies
    UserName = session.get('https://www.roblox.com/my/settings/json').json()['Name']
    UserId = session.get('https://www.roblox.com/my/settings/json').json()['UserId']
    print("Login As (.ROBLOSECURITY) : "+UserName+" | "+str(UserId))

if cookies == "YOUR_.ROBLOSECURITY_HERE" :
    print("Can't login , Please edit .ROBLOSECURITY cookie first")
else :
    LoginAs()

def toascii(text):
    ascii_art = pyfiglet.figlet_format(text,font="standard")
    print(ascii_art)

gentext = "RBLX LtdBY"
toascii(gentext)

print("Python Limited Buyer [By : FujaTyping]")
print("0. Edit config.json\n1. DankoOfficial\n2. Zentred [Working]\n3. FujaTyping Custom [Working]\n")

Want = int(input("Enter number : "))

if Want == 0 :
    print("You select : Edit config.json\n")
    print("Edit cookie [JSON]")
    Cookie = input("Enter .ROBLOSECURITY cookie : ")

    with open('config.json', 'r') as file:
        data = json.load(file)

    data['cookie'] = Cookie

    with open('config.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("\nUpdate .ROBLOSECURITY cookie finish")

elif Want == 1 :
    print("You select : DankoOfficial\n")
    exec(open("DankoOfficial.py").read())
elif Want == 2 :
    print("You select : Zentred\n")
    exec(open("Zentred.py").read())
elif Want == 3 :
    print("You select : FujaTyping Custom\n")
    exec(open("FujaTyping.py").read())
else :
    print("Please select number 0 or 1 or 2 or 3")