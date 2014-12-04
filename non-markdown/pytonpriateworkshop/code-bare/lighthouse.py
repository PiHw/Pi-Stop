#!/usr/bin/python3
#lighthouse.py
import time
import RPi.GPIO as GPIO

#HARDWARE SETUP
# Model+ P1
# 2[=========XGYR]26
# 1[=============]25
LED=[26,24,22] #RED, YELLOW, GREEN
# Model+ P1
# 2[===============XGYR]40
# 1[===================]39
#LED=[40,38,36] #RED, YELLOW, GREEN (uncomment to use)

FLASH_TIME=0.3
RED,YELLOW,GREEN=0,1,2
ON,OFF=True,False

def GPIOsetup():
   GPIO.setmode(GPIO.BOARD)
   for led in (RED,YELLOW,GREEN):
      GPIO.setup(LED[led],GPIO.OUT)

def ShowSignal(state):
   for led in (RED,YELLOW,GREEN):
      if (state[led]):
         print("# ",end="")
      else:
         print("  ",end="")
   print("")

def ControlLights(state):
   for led in (RED,YELLOW,GREEN):
      GPIO.output(LED[led],state[led])
   time.sleep(FLASH_TIME)

def SendLighthouseSignal(signalRED,signalYELLOW,signalGREEN):
   numItems=[]
   allsignals=[signalRED,signalYELLOW,signalGREEN]
   for signal in allsignals:
      numItems.append(len(signal))
   for i in range(max(numItems)):
      state=[]
      for led in (RED,YELLOW,GREEN):
         try:
            state.append(allsignals[led][i])
         except IndexError:
            state.append(OFF)
      ShowSignal(state)
      ControlLights(state)

GPIOsetup()