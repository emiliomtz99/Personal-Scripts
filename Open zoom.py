from datetime import datetime
import subprocess
import pyperclip


var = 1
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    start = '08:58:00'
    end = '09:03:00'
    start2 = '1:58:00'
    end2 = '02:03:00'
    if current_time > start and current_time < end and var == 1:
        subprocess.Popen('C:/Users/emmartinez/AppData/Roaming/Zoom/bin/Zoom.exe')
        pyperclip.copy('476923')
        var = 2
    else:
        if current_time > start2 and current_time < end2 and var == 2:
        subprocess.Popen('C:/Users/emmartinez/AppData/Roaming/Zoom/bin/Zoom.exe')
        pyperclip.copy('476923')
        var = 1