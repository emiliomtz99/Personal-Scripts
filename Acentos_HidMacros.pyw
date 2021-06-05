import time
import subprocess
import os

os.system('TASKKILL /f /IM HidMacros.exe')
time.sleep(3)
subprocess.call("C:/Users/Emilio/Documents/HidMacros/HidMacros.exe")

