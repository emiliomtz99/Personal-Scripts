"""
Simulate clicking and comparing images to know if has or dowsnt have subs, 
if youtube ia change run this code:

im1 = ImageGrab.grab(bbox  =(1357, 715, 1570, 748))
im1 = im1.save("Youtubeimg1.png") 

If wanna know the location of a pixel box:
from pynput.mouse import Button, Controller
mouse = Controller()
print(mouse.position) 
#you can check 2 corners and change the bbox parameters accordingly 
"""
from PIL import Image, ImageChops, ImageGrab
from pynput.mouse import Button, Controller
import time


img1 = Image.open('C:/Users/emartinezbarajas/Documents/Personal Scripts/Youtubeimg1.png')
img2 = ImageGrab.grab(bbox  =(1357, 715, 1570, 748))


diff = ImageChops.difference(img1, img2)

if diff.getbbox():
	#diff.show()
	mouse = Controller()
	mouse.position = (1431, 726) 	#SETTINGS	WITH SUBS
	mouse.click(Button.left)
	time.sleep(.2)
	mouse.position = (1431, 581) 	#SPEED
	mouse.click(Button.left)
	time.sleep(.4)
	mouse.position = (1431, 669) 	#x2
	mouse.click(Button.left)
	time.sleep(.3)
	mouse.position = (1551, 731) 	#Fullscreen
	mouse.click(Button.left)
	time.sleep(.2)


else:
	mouse = Controller()
	mouse.position = (1431, 726) 	#SETTINGS	NORMAL
	mouse.click(Button.left)
	time.sleep(.2)
	mouse.position = (1431, 630) 	#SPEED
	mouse.click(Button.left)
	time.sleep(.4)
	mouse.position = (1431, 669) 	#x2
	mouse.click(Button.left)
	time.sleep(.3)
	mouse.position = (1551, 731) 	#Fullscreen
	mouse.click(Button.left)
	time.sleep(.2)
