from pynput.mouse import Button, Controller
import time
mouse = Controller()

#Minimize all
mouse.move (1600, 900)
print('Now we have moved it to {0}'.format(mouse.position))
mouse.click(Button.left)
time.sleep(.1)


#Right click desktop
mouse.position = (800, 450)
print('Now we have moved it to {0}'.format(mouse.position))
mouse.press(Button.right)
mouse.release(Button.right)
time.sleep(.1)

#Click Button
mouse.position = (884, 689)
print('Now we have moved it to {0}'.format(mouse.position))
mouse.click(Button.left)
time.sleep(1)



#Scroll Down
mouse.scroll(0, -7)
time.sleep(.1)

#Click Display thingy
mouse.position = (507, 602)
print('Now we have moved it to {0}'.format(mouse.position))

time.sleep(.1)
mouse.press(Button.left)
mouse.release(Button.left)