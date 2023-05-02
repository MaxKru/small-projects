# Import necessary libraries
from machine import ADC, Pin, PWM
from time import sleep

# Configure ADC for joystick
adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

# Configure LED pin
led = PWM(Pin(14), freq=1000)

# Loop to read joystick input and control LED brightness
while True:
  # Read joystick x-axis input
  x = adc.read()
  
  if(x>3000):
    x-=1000
    
  if(adc.read()>3094):
    x = adc.read()
    
    
  
  print(x)
  sleep(0.2)
  # Convert joystick x-axis input to brightness value
  duty_cycle = int(x * (100 / 4096))
  
  # Set LED brightness
  print(duty_cycle)
  led.duty(duty_cycle)
