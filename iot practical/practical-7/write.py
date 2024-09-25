import RPi.GPIO as GPIO 
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	text = input("Enter new Data on the card")
	print("Now place the card")
	reader.write(text)
	print("Data written successfully")

finally:
	GPIO.cleanup()


