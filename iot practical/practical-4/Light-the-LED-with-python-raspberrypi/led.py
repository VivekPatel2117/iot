import RPi GPIO as GPIO 
import time 

GPIO.setMode(GPIO.BCM)
GPIO.setWarnings(False)
GPIO.setup(18,GPIO.OUT)
print("LED On")
GPIO.output(18,GPIO.HIGH)
time.sleep(5)
print("LED Off")
GPIO.output(18,GPIO.LOW)
