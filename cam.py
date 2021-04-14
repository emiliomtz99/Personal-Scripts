import cv2
import time  
  
# define a video capture object
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
image_path = r'C:\Users\Emilio\Desktop\geeks.png'

time.sleep(5)
ret, frame = vid.read()

 

cv2.imwrite(r'C:\Users\Emilio\Desktop\geeks.png', frame)

