from machine import Pin, UART, Timer
from time import sleep_ms, sleep_us, ticks_us, ticks_ms

led = Pin(19, Pin.OUT)
uartm = UART(2, baudrate=9600)
trigger=Pin(12, Pin.OUT)
echo=Pin(14, Pin.IN)
Tmess = Timer(0)

print("programm start")

def irrTmess(timer):
	trigger.on()
	sleep_us(20)
	trigger.off()  
	while echo.value() == 0:
		pass
	ticks1 = ticks_us()
	while echo.value() == 1:
		pass
	ticks2 = ticks_us()
	cm = (ticks2 - ticks1) /58
	uartm.write(str(cm) + " cm entfernung")

while True:
	inputm = uartm.read()
	if inputm:
		inputm = inputm.decode('utf-8')
	if inputm == "messen":
		uartm.write("messung wird gestartet")
		Tmess.init(period = 2000,mode = Timer.PERIODIC,callback = irrTmess)
	elif inputm == "stop":
		uartm.write("messung wird gestoppt")
		Tmess.deinit()




