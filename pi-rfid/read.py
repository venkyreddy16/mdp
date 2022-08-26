#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
	id, bal = reader.read()
	print(id)
        #print(text)
	print(bal)
finally:
	GPIO.cleanup()
