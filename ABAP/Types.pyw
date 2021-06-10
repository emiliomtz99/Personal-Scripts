from pynput.keyboard import Key, Controller
import keyboard
import time
Pkeyboard = Controller()

keyboard.write('TYPES: BEGIN OF ty_ejemplo,')
Pkeyboard.press(Key.enter)
keyboard.write('        campo1    TYPE i')
Pkeyboard.press(Key.enter)
keyboard.write('        campo2    TYPE i')
Pkeyboard.press(Key.enter)
keyboard.write('        campo3    TYPE i')
Pkeyboard.press(Key.enter)
keyboard.write('TYPES: END OF ty_ejemplo.')
Pkeyboard.press(Key.enter)



Pkeyboard.press(Key.up)
time.sleep(.05)
Pkeyboard.press(Key.up)
time.sleep(.05)
Pkeyboard.press(Key.up)
time.sleep(.05)
Pkeyboard.press(Key.up)
time.sleep(.05)
Pkeyboard.press(Key.up)

Pkeyboard.press(Key.end)
time.sleep(.05)
Pkeyboard.press(Key.left)











