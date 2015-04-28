#!/usr/bin/python
import serial

ser=serial.Serial('/dev/ttyAMA0',38400)

def go(x,y):
 ser.write(chr(128))
 ser.write(chr(6))
 ser.write(chr(x))
 ser.write(chr((128+6+x)&0x7F))
 ser.write(chr(128))
 ser.write(chr(7))
 ser.write(chr(y))
 ser.write(chr((128+7+y)&0x7F))

x=[0,30,50,64,74,90,127]

go(64,64)
while 1:
 

