from machine import Pin
from time import sleep, sleep_us, ticks_us
trigger=Pin(5, Pin.OUT)

echo=Pin(4, Pin.IN)
  
while True:  
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
  sleep(0.25)