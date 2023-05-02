from machine import Pin, Timer
from time import sleep, sleep_us, ticks_us, ticks_ms

trigger=Pin(12, Pin.OUT)
echo=Pin(14, Pin.IN)
taster=Pin(27, Pin.IN, Pin.PULL_UP)
status = True
timer1 = Timer(0)

def irrtaster(Pin_nr):
	global status
	status = not status
	if status == True:
		timer1.init(period = 1000,mode = Timer.PERIODIC,callback = irrtimer)
	else:	
		timer1.deinit()

def irrtimer(Timer):
  trigger.on()
  sleep_us(10)
  trigger.off()
  
  while echo.value() == 0:
	pass
  ticks1 = ticks_us()
  while echo.value() == 1:
	pass
  ticks2 = ticks_us()
  cm = (ticks2 - ticks1)  /  58.0
  print(cm, " cm")
  file = open ("distanz.txt","w")
  file.write(int(cm) + " cm")
  

taster.irq(trigger = Pin.IRQ_RISING, handler = irrtaster)
