#!/usr/bin/python3
# display.py
#
import pistop.pistop as PS
import time

WAIT=1

class display():
  def __init__(self, hw_id=("A+","A","C","D","B","B+"),DEBUG=False):
    '''Init display hw'''
    self.DEBUG=DEBUG
    self.hw=[]
    #Add hw id's to the display hw
    for id in hw_id:
      self.hw.append(PS.PiStop(id,DEBUG=self.DEBUG))
    self.LEDS=len(PS.ALL)
    self.PISTOPS=len(self.hw)
    self.TOTAL=self.PISTOPS*self.LEDS
    
  def __enter__(self):
    '''Enter: Set all ON and then all OFF'''
    if self.DEBUG:print("Enter display Class")
    #Set all ON
    for i in self.hw:
      i.output(PS.ALL,PS.ON)
    time.sleep(WAIT)
    #Set all OFF
    for i in self.hw:
      i.output(PS.ALL,PS.OFF)
    return self

  def __exit__(self,type,value,traceback):
    '''Switch OFF and Clean up PiStops'''    
    if self.DEBUG:print("Class display Exit")
    #Set all OFF
    if self.DEBUG:print("Set all OFF")
    for i in self.hw:
      i.output(PS.ALL,PS.OFF)
    PS.GPIO.cleanup()
    
  def coord(self,x=0,y=0,state=PS.ON):
    '''
    Control PiStop(s) by coordinates x=PiStop Position y=G/Y/R
    i.e. x,y = 3,0
    
       R 2 o  o  o  #
    y  Y 1 o  o  o  o
       G 0 o  o  o  o
           0  1  2  3
              x
    '''
    self.hw[x].output(y,state)

  def pos(self,pos=0,state=PS.ON,vertical=False):
    '''
       Control PiStop(s) by position
       i.e. 0-2 1st PiStop
            3-5 2nd PiStop
            6-8 3rd PiStop
    '''
    #Limit pos to not exceed total leds
    _pos=int(pos%self.TOTAL)
    if(vertical):
      if self.DEBUG:print("Order Vertically")
      _pistop=int(_pos/self.LEDS)
      _led=int(_pos%self.LEDS)
    else:
      if self.DEBUG:print("Order Horizontally")
      _pistop=int(_pos%self.PISTOPS)
      _led=int(_pos/self.PISTOPS)    
    if self.DEBUG:print("Pos: {}\tState: {}\tPiStop: {}\tLight: {}".format(pos,state,_pistop,_led))
    self.coord(_pistop,_led,state)

  def demoSpin(self,cw=True,delay=WAIT/10):
    '''Display Spinning LEDs Demo'''
    spin=[[[0,0],[1,1],[2,2]], #/
          [[0,1],[1,1],[2,1]], #-
          [[0,2],[1,1],[2,0]], #\
          [[1,0],[1,1],[1,2]], #|
          [[0,0],[1,1],[2,2]], #/
          [[0,1],[1,1],[2,1]], #-
          [[0,2],[1,1],[2,0]], #\
          [[1,0],[1,1],[1,2]]] #|
    if cw==False:
      spin.reverse()
    SIDE=int(self.PISTOPS/2)
    #Display each row
    for row in spin:
      for j in row:
        self.coord(j[0],j[1],PS.ON)
        self.coord(j[0]+SIDE,j[1],PS.ON)
      time.sleep(delay)
      for j in row:
        self.coord(j[0],j[1],PS.OFF)
        self.coord(j[0]+SIDE,j[1],PS.OFF)

  def demoLine(self,vertical=False,delay=WAIT/10):
    '''Display Lines LED Demo'''
    if vertical:
      #Vertical
      for x in range(self.PISTOPS):
        for y in range(self.LEDS):
          self.coord(x,y,PS.ON)
        time.sleep(delay)
        for y in range(self.LEDS):
          self.coord(x,y,PS.OFF)
    else:
      #Horizontal
      for y in range(self.LEDS):
        for x in range(self.PISTOPS):
          self.coord(x,y,PS.ON)
        time.sleep(delay)
        for x in range(self.PISTOPS):
          self.coord(x,y,PS.OFF)

#Test module
if __name__ == "__main__":
  with display(DEBUG=False) as pistopdis:
    print("Created PiStop Display")
    pistopdis.coord(0,0,PS.ON)
    pistopdis.coord(1,0,PS.ON)
    pistopdis.coord(2,0,PS.ON)
    time.sleep(WAIT)
    pistopdis.coord(0,0,PS.OFF)
    pistopdis.coord(1,0,PS.OFF)
    pistopdis.coord(2,0,PS.OFF)
    time.sleep(WAIT)
    pistopdis.pos(2)
    pistopdis.pos(5)
    pistopdis.pos(8)
    time.sleep(WAIT)
    pistopdis.pos(2,PS.OFF)
    pistopdis.pos(5,PS.OFF)
    pistopdis.pos(8,PS.OFF)
    time.sleep(WAIT)

    #Cycle through all LEDs
    print("Cycle through all LEDs")
    #Horizontal
    for i in range(100):
      pistopdis.pos(i,PS.ON)
      time.sleep(WAIT/20)
      pistopdis.pos(i,PS.OFF)
    #Vertical
    for i in range(100):
      pistopdis.pos(i,PS.ON,True)
      time.sleep(WAIT/20)
      pistopdis.pos(i,PS.OFF,True)

    #Cycle through lines
    print("Cycle through lines")
    #Vertical
    print("Vertical")
    for i in range(10):
      pistopdis.demoLine(vertical=True)
    #Horizontal
    print("Horizontal")
    for i in range(10):
      pistopdis.demoLine(vertical=False)

    #Spin
    print("Spin CW")
    for i in range(20):
      pistopdis.demoSpin()
    print("Spin Anti-CW")
    for i in range(20):
      pistopdis.demoSpin(cw=False)
        