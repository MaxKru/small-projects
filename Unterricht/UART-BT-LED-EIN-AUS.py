from machine import Pin, UART
from time import sleep_ms

led = Pin(19, Pin.OUT)
uart = UART(2, baudrate=9600)

print(uart)

falscheeingabe = False

def Weingabe():
	global falscheeingabe
	if falscheeingabe == True:
		uart.write("falschen string eingegeben")
		sleep_ms(500)
	falscheeingabe = False



while True:
	zeichen1 = uart.any()
	print(zeichen1)
	
	zeichen2 = uart.read()
	print(zeichen2)
	
	if zeichen2:
		zeichen2 = zeichen2.decode('utf-8')
		if(zeichen2 == 'LED AN'):
			led.value(1)
		elif(zeichen2 == 'LED AUS'):
			led.value(0)
		elif(zeichen2 != 'LED AN'):
			falscheeingabe = True
		elif(zeichen2 != 'LED AUS'):
			falscheeingabe = True
	Weingabe()
	
	print("warte..")
	uart.write("sende einen String")
	sleep_ms(500)
	