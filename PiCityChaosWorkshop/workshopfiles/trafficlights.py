#!/usr/bin/python3
# trafficlights.py
#
# For workshops and further details see https://github.com/PiHw/Pi-Stop
# The PiStop is designed and produced jointly by PiHardware and 4Tronix
#
# Use "from ... import *" to directly import
# the pistop module into the code.
from pistop.pistop import *
import time

#Crazy Light show
def crazylights(pistop):
  pistop.output(r,off)
  pistop.output(g,on)
  time.sleep(0.2)
  pistop.output(g,off)
  pistop.output(y,on)
  time.sleep(0.2)
  pistop.output(y,off)
  pistop.output(r,on)
  time.sleep(0.2)

#Main Code
print("PiCity Chaos!")
with PiStop(hwSetup="A") as myps:
  myps.output(all,on)
  time.sleep(2)
  myps.output(all,off)
  time.sleep(2)
  while True:
    crazylights(myps)
