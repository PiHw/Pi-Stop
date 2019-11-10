#!/usr/bin/python3
# gpiopins.py
#
# Allow support for GPIO.BOARD in GPIOZero
# Use as follows:
#   import gpiopins as GPIO
#   GPIO.setmode(GPIO.BOARD)
# GPIOZero will default to GPIO.BCM
#
# Tim Cox (meltwater)

from os import environ
BCM=11
BOARD=10

def setmode(mode=BCM):
  if mode==BOARD:
    #Note: The environ value will not remain after the script
    #      has completed.
    #      GPIOZERO will default back to BCM next time it is used.
    environ["GPIOZERO_BOARD"]="Using BOARD pin numbers"
  else:
    #Allow users to change the pin numbering mode back to BCM
    #(although this will happen anyway when the script finishes)
    try:
      del environ["GPIOZERO_BOARD"]
    except KeyError:
      return
