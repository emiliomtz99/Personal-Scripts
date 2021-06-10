from pynput.keyboard import Key, Controller
import keyboard
import pyautogui
import time
Pkeyboard = Controller()

keyboard.write('CLASS ClassName DEFINITION.')
Pkeyboard.press(Key.enter)
keyboard.write('  PUBLIC SECTION.')
Pkeyboard.press(Key.enter)
keyboard.write('  DATA: VarName  TYPE CHAR20,')
Pkeyboard.press(Key.enter)
keyboard.write('        VarName2 TYPE CHAR10,')
Pkeyboard.press(Key.enter)
keyboard.write('  METHODS: MethodName IMPORTING VarName TYPE CHAR20 VarName2 TYPE CHAR10 .')
Pkeyboard.press(Key.enter)
keyboard.write('ENDCLASS.')
Pkeyboard.press(Key.enter)

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