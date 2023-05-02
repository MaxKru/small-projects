#test übungen
from machine import Pin, Timer
from time import sleep, ticks_ms

led = Pin(17,Pin.OUT,value=0)
taster = Pin(16,Pin.IN,Pin.PULL_UP)


status = False
zähler = 0
altzeit = 0

def irrtaster(Pin_nr):
	global status, altzeit
	aktzeit = ticks_ms()
	if(aktzeit - altzeit) >100:
		status = not status
		altzeit = aktzeit
#
def irrtimer(Timer):
	global status, zähler
	status = not status
	if zähler =10:
		timer1.deinit()
	zähler +=1
#

#wert der led wird jede sek getauscht
def irrtimer2(Timer):
	led.value(not led.value())
	
#
taster.irq(trigger = Pin.IRQ_RISING, handler = irrtaster)

timer1 = Timer(0)

timer1.init(period = 1000,mode = Timer.PERIODIC,callback = irrtimer)



while True:
	if status == 1:
		led.value(1)
		sleep(0.25)
		led.value(0)
		sleep(0.25)
	else:
		led.value(0)
#
