from pynput.keyboard import Key, Controller
import keyboard
import pyautogui
import time
Pkeyboard = Controller()

keyboard.write('CLASS ClassName IMPLEMENTATION.')
Pkeyboard.press(Key.enter)
keyboard.write('  METHOD MethodName.')
Pkeyboard.press(Key.enter)
keyboard.write('"******TYPE CODE HERE.******')
Pkeyboard.press(Key.enter)
Pkeyboard.press(Key.enter)
keyboard.write('  ENDMETHOD.')
Pkeyboard.press(Key.enter)
keyboard.write('ENDCLASS.')


Pkeyboard.press(Key.up)
time.sleep(.03)
Pkeyboard.press(Key.up)
time.sleep(.03)
Pkeyboard.press(Key.up)
time.sleep(.03)
Pkeyboard.press(Key.up)
time.sleep(.03)
Pkeyboard.press(Key.up)
time.sleep(.03)
Pkeyboard.press(Key.up)
time.sleep(.03)
pyautogui.hotkey('ctrl', 'right')
time.sleep(.03)
pyautogui.hotkey('ctrl', 'right')
time.sleep(.03)
Pkeyboard.press(Key.left)



"""

CLASS NAME DEFINITION.
  PUBLIC SECTION.
  DATA: NAME TYPE CHAR20,
        COLOR TYPE CHAR10,
  METHODS: CONSTRUCTOR IMPORTING NAME TYPE CHAR20 COLOR TYPE CHAR10 .
ENDCLASS.

"""