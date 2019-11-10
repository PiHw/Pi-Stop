import sys, pygame
import time

G,Y,R=g,y,r=0,1,2
OFF,ON=off,on=0,1

ALL=all=(G,Y,R)
status=[OFF,OFF,OFF]
RPI_REVISION=3

#Set DEBUG to True to display pins and status information
DEBUG=False

#Hardware Setup
location={"A":[22,24,26],
          "B":[23,21,19],
          "C":[8,10,12],
          "D":[7,5,3]}
locPlus={"A+":[36,38,40],
           "B+":[37,35,33]}
location=dict(list(location.items())+list(locPlus.items()))

#pins=location["A"]
pinsAll = [[22,24,26],
           [23,21,19],
           [8,10,12],
           [7,5,3],
           [36,38,40],
           [37,35,33]]

BOARD=1
OUT,IN=1,0

iON = [pygame.image.load("pistop\G.png"),
       pygame.image.load("pistop\Y.png"),
       pygame.image.load("pistop\R.png")]
rect = [iON[G].get_rect(),
        iON[Y].get_rect(),
        iON[R].get_rect()]

pistop = pygame.image.load("pistop\pi-Stop.png")
pistoprect = pistop.get_rect()

def setmode(mode):
    pass

def setup(pin,mode):
    pass

def cleanup():
    pass

def output(pin,state):
    global status
    if DEBUG:print("Pin:%s State:%s" %(pin,state))
    for loc in pinsAll:
        for i,val in enumerate(loc):
            if val==pin:
                status[i]=state    
    #for i,val in enumerate(pins):
    #  if val==pin:
    #    status[i]=state
    if DEBUG:print(status)
    update()    

def update():
    screen.blit(pistop, pistoprect)
    for i in ALL:
      if status[i]==ON:
        screen.blit(iON[i], rect[i])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

pygame.init()
size = width, height = 103, 458
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
screen.fill(white)

if __name__ == '__main__':
  while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    output(21,ON)
    time.sleep(1)
    #update()
    output(21,OFF)
    time.sleep(1)
