#!/usr/bin/python3
# trafficlights-solvepython02.py
#
# For workshops and further details see https://github.com/PiHw/Pi-Stop
# The PiStop is designed and produced jointly by PiHardware and 4Tronix
#
# Use "from ... import *" to directly import
# the pistop module into the code.
from pistop.pistop import *
import time

def trafficSTOP(pistop):
  ''' STOP = ->YELLOW->RED '''
  pistop.output(r,off)
  pistop.output(y,on)
  pistop.output(g,off)
  time.sleep(0.2)
  pistop.output(r,on)
  pistop.output(y,off)
  pistop.output(g,off)
  time.sleep(0.2)

def trafficGO(pistop):
  ''' GO = ->RED+YELLOW->GREEN '''
  pistop.output(r,on)
  pistop.output(y,on)
  pistop.output(g,off)
  time.sleep(0.2)
  pistop.output(r,off)
  pistop.output(y,off)
  pistop.output(g,on)
  time.sleep(0.2)

#Main Code
print("PiCity Chaos!")
with PiStop(hwSetup="A") as myps:
  myps.output(all,on)
  time.sleep(2)
  myps.output(all,off)
  time.sleep(2)
  while True:
    trafficSTOP(myps)
    time.sleep(5)
    trafficGO(myps)
    time.sleep(5)