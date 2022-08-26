#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	#text = input('New data:')
	bal = '50'
	print("Now place your tag to write")
	#reader.write(text)
	reader.write(bal)
	print("Written")

finally:
	GPIO.cleanup()
