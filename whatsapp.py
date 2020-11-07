import pywhatkit as kit
from tkinter import filedialog



msg = input("Enter massege: ")
num = input("Enter phone: ")

import datetime

def to_string_function(val):
    return str(val)


def sessionCalculator():
    dt = datetime.datetime.today()
    time=datetime.datetime.now().time().replace(microsecond=0)

    return time

print(to_string_function(sessionCalculator().hour) + " min " + to_string_function(sessionCalculator().minute+1))

#kit.search("Python")
#filedirectory = filedialog.askdirectory()
#kit.image_to_ascii_art('D:\python\whatsapp\lewis.png',"luja.png")

#search= input("what do you want to search? ")

#text = kit.info(search,lines=4)

#kit.text_to_handwriting(text,rgb=[0,0,0])
kit.sendwhatmsg(num, msg, sessionCalculator().hour, sessionCalculator().minute+1)

#kit.shutdown(time=100)

#kit.shutdown(time=100)

#kit.help()