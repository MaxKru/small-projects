'''
EEPROM

einen festen anteil der RefV


'''

from machine import Pin, SoftI2C, ADC
from time import sleep
from random import randint

adw = ADC(Pin(34))
adw.atten(ADC.ATTN_11DB)
adw.width(ADC.WIDTH_12BIT)


bus = SoftI2C(scl = Pin(22), sda = Pin(21))

gerate = bus.scan()

print(type(gerate))

for x in gerate:
	print(gerate)

wb = bytearray(3)


'''
config		HIGH		LOW
00000000	00000000	0000000

D 4096 max.

hälfte 2048

config bleibt gleich

00000000.0000xxxx

wert = int(bin(4095))

high = wert >>4
low = wert <<4

'''


config  = 0b01100000
high	= 0b10000000
low		= 0b00000000

wb[0] = config
wb[1] = high
wb[2] = low
  
bus.writeto(96, wb)

while True:
	
	maxV = 3300
	proz = 0
	
	rnd = randint(0,4095)
	
	wert =  rnd / 4095 * 3300
	
	high  = rnd >> 4
	low  = rnd << 4
	config  = 96
	
	
	wb[0] = config
	wb[1] = int(high)
	wb[2] = int(low)
    
	bus.writeto(96, wb)
	
	mess = adw.read()
	messmv = mess * 3300 / 4095
	#print(mess)
	print(" %d mV" %messmv)
	sleep(1)
	
	
	

#int_val = int.from_bytes(wb, 'big')






