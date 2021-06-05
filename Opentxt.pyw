import subprocess as sp
import os

programName = "notepad.exe"
fileName1 = "C:/Users/emmartinez/Desktop/Zoom.txt"
fileName2 = "C:/Users/emmartinez/Desktop/Academia/Transacciones.txt"

f = open("var.txt", "r")
Op = (f.read(1))
if Op == "1":
	sp.Popen([programName, fileName1])
	sp.Popen([programName, fileName2])

	f = open("var.txt", "w")
	f.write("2")
	
if Op == "2":
	os.system('TASKKILL /f /IM notepad.exe')

	f = open("var.txt", "w")
	f.write("1")