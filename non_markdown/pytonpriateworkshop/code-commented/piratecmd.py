#!/usr/bin/python3

import sys
import time
import pythonpirate

if (len(sys.argv)==2):
   print("Args: ", sys.argv[1])
   while(1):
      pythonpirate.PlayMessage(sys.argv[1])
      time.sleep(1)