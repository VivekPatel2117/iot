import picamera 
from time import sleep
cam = picamera.PiCamera()

cam.start_preview()

cam.hflip = True
cam.vflip = True
sleep(5)

cam.capture("image.png")
for i in range():
	sleep(5)
	cam.capture(f"image{i}.png")
cam.stop_preview()

