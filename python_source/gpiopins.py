#!/usr/bin/python3
# gpiopins.py
#
# Proof of concept, BOARD to PCM conversion for GPIOZero

#Convert BCM to Pins
#Pin Types
V5  = None
V3_3 = None
ID = None
GND = None

pin=[None,
     V3_3, V5,
     2,    V5,
     3,    GND,
     4,    14,
     GND,  15,
     17,   18,
     27,   GND,
     22,   23,
     V3_3, 24,
     10,   GND,
     9,    25,
     11,   8,
     GND,  7,
     ID,   ID,
     5,   GND,
     6,   12,
     13,  GND,
     19,   16,
     26,   20,
     GND,  21
     ]


#Pins numbering to BCM GPIO
p01 = pin[1];  p02 = pin[2]
p03 = pin[3];  p04 = pin[4]
p05 = pin[5];  p06 = pin[6]
p07 = pin[7];  p08 = pin[8]
p09 = pin[9];  p10 = pin[10]
p11 = pin[11]; p12 = pin[12]
p13 = pin[13]; p14 = pin[14]
p15 = pin[15]; p16 = pin[16]
p17 = pin[17]; p18 = pin[18]
p19 = pin[19]; p20 = pin[20]
p21 = pin[21]; p22 = pin[22]
p23 = pin[23]; p24 = pin[24]
p25 = pin[25]; p26 = pin[26]
####################
p27 = pin[27]; p28 = pin[28]
p29 = pin[29]; p30 = pin[30]
p31 = pin[31]; p32 = pin[32]
p33 = pin[33]; p34 = pin[34]
p35 = pin[35]; p36 = pin[36]
p37 = pin[37]; p38 = pin[38]
p39 = pin[39]; p40 = pin[40]

#Alias
P01=P1=p1=p01
P02=P2=p2=p02
P03=P3=p3=p03
P04=P4=p4=p04
P05=P5=p5=p05
P06=P6=p6=p06
P07=P7=p7=p07
P08=P8=p8=p08
P09=P9=p9=p09
P10=p10
P11=p11
P12=p12
P13=p13
P14=p14
P15=p15
P16=p16
P17=p17
P18=p18
P19=p19
P20=p20
P21=p21
P22=p22
P23=p23
P24=p24
P25=p25
P26=p26
P27=p27
P28=p28
P29=p29
P30=p30
P31=p31
P32=p32
P33=p33
P34=p34
P35=p35
P36=p36
P37=p37
P38=p38
P39=p39
P40=p40

if __name__ == '__main__':
    print("Pin\tGPIO\tGPIO\tPin")
    for i in range(1,21):
        print("%s\t%s\t%s\t%s"%((2*i)-1,pin[(2*i)-1],pin[2*i],2*i))
