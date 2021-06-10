from pynput.keyboard import Key, Controller
import keyboard
import pyautogui
import time
Pkeyboard = Controller()

keyboard.write('DATA: lv_ejemplo TYPE ty_ejemplo.')

Pkeyboard.press(Key.home)

time.sleep(.1)
pyautogui.hotkey('ctrl', 'right')
time.sleep(.05)
pyautogui.hotkey('ctrl', 'right')
time.sleep(.05)
Pkeyboard.press(Key.left)
time.sleep(.05)
Pkeyboard.press(Key.down)

