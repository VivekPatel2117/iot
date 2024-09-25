#Configuration of raspi
#sudo apt-get update
#sudo apt-get intsall python-pip
#sudo pip install telepot


#CODE
import RPi.GPIO as GPIO
import time
import sys
import random
from telepot.loop import MessageLoop
import telepot

def ON(pin):
	GPIO.output(pin,GPIO.HIGH)
	return
def OFF(pin):
	GPIO.output(pin,GPIO.LOW)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['txt']
	print('received: %s' % commond)

	if commond == "ON":
		GPIO.output(11,GPIO.HIGH)
	elif commond == 'OFF':
		GPIO.output(11,GPIO.LOW)
bot = telepot.BOT("TOKEN")
MessageLoop(bot,handle).run_as_thread()
print("I'm listening")

while(1):
	time.sleep(1)

