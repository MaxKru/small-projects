from machine import Pin, Timer
from time import sleep, sleep_us, ticks_us

trigger=Pin(12, Pin.OUT, value = 0)
echo=Pin(14, Pin.IN)
taster=Pin(27, Pin.IN, Pin.PULL_UP)

timer1 = Timer(0)

def isrTimer(tim):
	trigger.on()
	sleep_us(10)
	trigger.off()
#

def isrMess(eco):
	tstart = ticks_us()
	while echo.value()==1:
		pass
	tstop = ticks_us()
	
	masz = (tstop - tstart) /2*343.2*10**2*10**-6 #58
	print("entfernung : %.1f" %masz)

echo.irq(trigger=Pin.IRQ_RISING, handler = isrMess)

timer1.init(period=1500 , mode=Timer.PERIODIC, callback=isrTimer)













