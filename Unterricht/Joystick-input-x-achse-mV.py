# Import necessary libraries
from machine import ADC, Pin
from time import sleep

# Configure ADC for joystick
adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)


while True:
	# Read joystick x-axis input
	x = adc.read()
	
	# Convert joystick x-axis input to mV
	x_mv = x * (3300 / 4096)
	
	# Print x-axis input in mV
	print("X-axis input: %d mV" % x_mv)
	sleep(0.4)
	
