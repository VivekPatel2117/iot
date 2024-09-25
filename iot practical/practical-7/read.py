import RPi.GPIO as GPIO 

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	id,text = reader.read()
	print(f"ID {id}")
	print(f"Text: {text}")
finally:
	GPIO.cleanup()

