import json
import pyfiglet

def toascii(text):
    ascii_art = pyfiglet.figlet_format(text,font="standard")
    print(ascii_art)

gentext = "RBLX LtdBY"
toascii(gentext)

print("Python Limited Buyer [By : FujaTyping]")
print("0. Edit config.json\n1. DankoOfficial\n2. Zentred [Working]\n")

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
else :
    print("Please select number 0 or 1 or 2")