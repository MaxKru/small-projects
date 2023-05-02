from machine import Pin, UART
from time import sleep_ms

led = Pin(19, Pin.OUT)
uartm = UART(2, baudrate=9600)
uarts = UART(1, baudrate=9600,tx=4,rx=0)

#4 0 selbs gesetzt

# uart1 = UART(1, baudrate=9600, tx=33, rx=32)
#		uart0	uart1	uart2
#	tx	1		10		17
#	rx	3		9		16


print(uartm)
print(uarts)

while True:
	zeichen1 = uartm.any()
	print(zeichen1)
	
	zeichen2 = uartm.read()
	print(zeichen2)
	
	if zeichen2:
		zeichen2 = zeichen2.decode('utf-8')
	
	if(zeichen2 == 'LED AN'):
		led.value(1)
	elif(zeichen2 == 'LED AUS'):
		led.value(0)
	
	print("warte..")
	uartm.write("sende nun einen String")
	sleep_ms(500)
	
	zeichen1 = uarts.any()
	print(zeichen1)
	
	zeichen2 = uarts.read()
	print(zeichen2)
	
	if zeichen2:
		zeichen2 = zeichen2.decode('utf-8')
	
	if(zeichen2 == 'LED AN'):
		led.value(1)
	elif(zeichen2 == 'LED AUS'):
		led.value(0)
	
	print("warte..")
	uarts.write("sende nun einen String Slave")
	sleep_ms(500)
	