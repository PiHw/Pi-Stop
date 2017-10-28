#!/usr/bin/python3
# trafficlights.py
#
import pistop as PS
import time

WAIT=1
DURATION=10

def run(pistop):
   pistop.output(PS.all,PS.OFF)
   time.sleep(5)
   pistop.output(PS.R,PS.ON)
   pistop.output((PS.Y,PS.G),PS.OFF)
   time.sleep(1)
   while(True):
      #Go
      pistop.output((PS.R,PS.Y),PS.ON)
      pistop.output(PS.G,PS.OFF)
      time.sleep(WAIT)
      pistop.output(PS.G,PS.ON)
      pistop.output((PS.R,PS.Y),PS.OFF)
      time.sleep(DURATION)
      #Stop
      pistop.output(PS.Y,PS.ON)
      pistop.output((PS.R,PS.G),PS.OFF)
      time.sleep(WAIT)
      pistop.output(PS.R,PS.ON)
      pistop.output((PS.Y,PS.G),PS.OFF)
      time.sleep(DURATION)

def go(pistop):
   #Go
   pistop.output((PS.R,PS.Y),PS.ON)
   pistop.output(PS.G,PS.OFF)
   time.sleep(WAIT)
   pistop.output(PS.G,PS.ON)
   pistop.output((PS.R,PS.Y),PS.OFF)

def stop(pistop):
   #Stop
   pistop.output(PS.Y,PS.ON)
   pistop.output((PS.R,PS.G),PS.OFF)
   time.sleep(WAIT)
   pistop.output(PS.R,PS.ON)
   pistop.output((PS.Y,PS.G),PS.OFF)


if __name__ == '__main__':
   with PS.PiStop("A") as myPiStopA,\
        PS.PiStop("B") as myPiStopB,\
        PS.PiStop("C") as myPiStopC,\
        PS.PiStop("D") as myPiStopD,\
        PS.PiStop("A+") as myPiStopAp,\
        PS.PiStop("B+") as myPiStopBp:
      while(1):
         #Stop: Lights D, A and B+
         stop(myPiStopD)
         stop(myPiStopA)
         stop(myPiStopBp)
         #Go:   Lights C, B and A+
         go(myPiStopC)
         go(myPiStopB)
         go(myPiStopAp)
         time.sleep(DURATION)
         
         #Stop: Lights C, B and A+
         stop(myPiStopC)
         stop(myPiStopB)
         stop(myPiStopAp)
         #Go:   Lights D, A and B+
         go(myPiStopD)
         go(myPiStopA)
         go(myPiStopBp)
         time.sleep(DURATION)
         
