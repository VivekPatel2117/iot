import RPi.GPIO as GPIO
import time
GPIO.setWarnings(False)
GPIO.setmode(GPIO.BCM)
p=GPIO.PWM(18,100)
p.start(0)
while(1):
	for x in range (50):
		p.ChangeDutyCycle(x)
		print("LED ON")
		time.sleep(0.0.1)
		for i in range(50):
			p.ChangeDutyCycle(50-X)
			print("LED OFF")
			time.sleep(0.01)
