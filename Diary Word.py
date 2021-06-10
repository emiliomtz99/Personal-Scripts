import shutil
from datetime import datetime
import os


now = datetime.now()

date_time = now.strftime("%d-%m-%Y")


with open('diaryVar.txt', 'r') as file:
    data = file.read()

name = data + ".-"+ date_time  +".docx"
shutil.copy('notes.docx', name) #Change to real folder"""


var = int(data)+1
f = open("diaryVar.txt", "w")
f.write(str(var))
f.close()

os.startfile(name)