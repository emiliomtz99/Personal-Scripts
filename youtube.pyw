import webbrowser
from pynput.mouse import Button, Controller
import time
import pyautogui
import os




mouse = Controller()
mouse.position = (1431, 726) 	#SETTINGS	
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
