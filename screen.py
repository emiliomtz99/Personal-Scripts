from pynput.mouse import Button, Controller
import time
from datetime import datetime
import pyautogui
import os

mouse = Controller()

#Check what i wanna do

f = open("screen.txt", "r")
Op = (f.read(1))

#change sound settings
mouse.position = (1430, 880) 	
mouse.click(Button.left)
time.sleep(.3)
mouse.position = (1427, 777) 	
mouse.click(Button.left)
time.sleep(.2)

if Op=="1":
	#change sound settings
	time.sleep(.2)
	mouse.position = (1402, 703) 	
	time.sleep(.2)
	mouse.click(Button.left)
	

if Op=="2":
	#change sound settings
	time.sleep(.2)
	mouse.position = (1402, 734)
	time.sleep(.2) 
	mouse.click(Button.left)


#Minimize all

mouse.position = (1600, 900)
#print('Now we have moved it to {0}'.format(mouse.position))
time.sleep(.1)
mouse.click(Button.left)
time.sleep(.1)


#Right click desktop
mouse.position = (800, 450)
#print('Now we have moved it to {0}'.format(mouse.position))
mouse.press(Button.right)
mouse.release(Button.right)
time.sleep(.1)



#Take SS
now = datetime.now()
 
joined_path = "C:\\Users\\Emilio\\Desktop\\Scripts\\Screepics\\" + now.strftime("%d.%m.%Y__%H.%M.%S") +".png"
s = pyautogui.screenshot()
s.save(joined_path)



#Click Button
mouse.position = (818, 735)
#print('Now we have moved it to {0}'.format(mouse.position))
mouse.click(Button.left)
time.sleep(1)


#Scroll Down
mouse.scroll(0, -7)
time.sleep(.2)

#Click Display thingy
mouse.position = (507, 602)
#print('Now we have moved it to {0}'.format(mouse.position))
time.sleep(.2)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(.3)

if Op=="1":
	
	#rename shurvut
	new=2
	f = open("screen.txt", "w")
	f.write("2")



	#Clck Show only 2nd
	mouse.position = (467, 665) 	
	time.sleep(.1)
	mouse.click(Button.left)
	
	#Click Okay
	time.sleep(.1)
	mouse.position = (941, 469)
	mouse.click(Button.left)

	#Change Variable in txt
	f = open("screen.txt", "w")
	f.write("2")


#	time.sleep(1)
#	mouse.position = (1575, 3)
#	mouse.click(Button.left)
	

if Op=="2":
	#rename shurvut
	new=1
	f = open("screen.txt", "w")
	f.write("1")

	
	#Clck Show extend	
	mouse.position = (500, 540)
	time.sleep(.1)
	mouse.click(Button.left)
	
	#Click Okay
	time.sleep(.3)
	mouse.position = (941, 469)
	mouse.press(Button.left)
	mouse.release(Button.left)


	#Change Variable in txt
	f = open("screen.txt", "w")
	f.write("1")

	

#rename shurvut
#print("C:\\Users\\Emilio\\Desktop\\screen" + str(Op) +".lnk")
os.rename("C:\\Users\\Emilio\\Desktop\\screen" + str(Op) +".lnk","C:\\Users\\Emilio\\Desktop\\screen" + str(new) +".lnk")


"""
Antes era 735
"""
