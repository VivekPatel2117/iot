import picamera 
import time 
cam = picamera.PiCamera()
cam.start_preview()
cam.start_recording("video.h264")
cam.annotate_text = "Hello!"
time.sleep(25)
cam.stop_recording()
cam.stop_preview()

