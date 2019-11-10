#!/usr/bin/python3
# testzero.py
#
# Example using GPIOZero with GPIO.BOARD numbering
# PiStop in Location C (BOARD pins 8,10,12)
#
# Note: 1. gpiopins.py must be located in python path or same directory.
#       2. /usr/lib/python3/dist-packages/gpiozero/devices.py should be updated as shown in devices.py file.

import gpiopins as GPIO
GPIO.setmode(GPIO.BOARD)

from gpiozero import LED
from time import sleep

green=LED(8)
yellow=LED(10)
red=LED(12)

green.blink()
sleep(0.1)
yellow.blink()
sleep(0.1)
red.blink()

