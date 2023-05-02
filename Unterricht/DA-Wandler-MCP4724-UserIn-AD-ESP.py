'''
EEPROM

einen festen anteil der RefV


'''

from machine import Pin, SoftI2C, ADC
from time import sleep

adw = ADC(Pin(34))
adw.atten(ADC.ATTN_11DB)
adw.width(ADC.WIDTH_12BIT)


bus = SoftI2C(scl = Pin(32), sda = Pin(33))

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
	'''
	print("halb")
	config  = 0b01100000
	high	= 0b10000000
	low		= 0b0000.0000

	wb[0] = config
	wb[1] = high
	wb[2] = low
  
	bus.writeto(96, wb)

	mess = adw.read()
	messmv = mess * 3300 / 4096
	#print(mess)
	print(" %d mV" %messmv)
	
	sleep(1)
	print("3/4")
	config  = 0b01100000
	high	= 0b11000000
	low		= 0b00000000

	wb[0] = config
	wb[1] = high
	wb[2] = low
  
	bus.writeto(96, wb)
	
	mess = adw.read()
	messmv = mess * 3300 / 4096
	#print(mess)
	print(" %d mV" %messmv)
	sleep(1)
	print("Voll")
	config  = 0b01100000
	high	= 0b11111111
	low		= 0b11111111

	wb[0] = config
	wb[1] = high
	wb[2] = low
  
	bus.writeto(96, wb)
	
	mess = adw.read()
	messmv = mess * 3300 / 4096
	#print(mess)
	print(" %d mV" %messmv)
	sleep(1)
	'''
	'''
	
	3.3V maximum
	4096 bits maximum
	um 1/2 * 3300V  = 1650 => das in bits wandeln -> 00000110 01110010
	
	'''	
	'''
	print("halb int")
	config  = 96
	high	= 128
	low		= 0

	wb[0] = config
	wb[1] = high
	wb[2] = low
  
	bus.writeto(96, wb)

	mess = adw.read()
	messmv = mess * 3300 / 4096
	#print(mess)
	print(" %d mV" %messmv)
	sleep(1)
	print("3/4 int")
	config  = 96
	high	= 192
	low		= 0

	wb[0] = config
	wb[1] = high
	wb[2] = low
  
	bus.writeto(96, wb)
	
	mess = adw.read()
	messmv = mess * 3300 / 4096
	#print(mess)
	print(" %d mV" %messmv)
	sleep(1)
	print("Voll int")
	config  = 96
	high	= 255
	low		= 255

	wb[0] = config
	wb[1] = high
	wb[2] = low
  
	bus.writeto(96, wb)
	
	mess = adw.read()
	messmv = mess * 3300 / 4096
	#print(mess)
	print(" %d mV" %messmv)
	sleep(1)
	'''
	
	maxV = 3300
	proz = 0
	UserV = input("miliVolt ausgabe?")
	print("ausgabe soll %s sein" %UserV)
	UserV = int(UserV)
	proz = 100 / maxV * UserV
	bits = 4095 * proz / 100
	print("%i sind %d %% von %d mV" % (UserV, proz, maxV))
	print("%d %% von 4095 ist: %d" % (proz, bits)) 

	config  = 96
	
	low = bits * 2**4
	high = bits / 2**4
	
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






