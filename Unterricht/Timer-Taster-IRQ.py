from machine import Pin, Timer
from time import sleep, ticks_ms


led = Pin(17,Pin.OUT,value=0)
taster = Pin(16,Pin.IN,Pin.PULL_UP)

status = False

def irrtaster(Pin_nr):
	status = not status
	if status = True:
		timer1.init(period = 1000,mode = Timer.PERIODIC,callback = irrtimer)
		print(str(timer1))
	else	
		timer1.deinit()

def irrtimer2(Timer):
	led.value(not led.value())
	
	#
taster.irq(trigger = Pin.IRQ_RISING, handler = irrtaster)

timer1 = Timer(0)

