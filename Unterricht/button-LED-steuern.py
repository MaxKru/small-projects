# Strom begrenzt auf 20mA
# Pins 32-39 nur als eingang

from machine import Pin
from time    import sleep, sleep_ms, sleep_us

#ms milisek
#us microsek

#1. Parameter = GPIO-Pin  -   general-purpose-input-output
#2. Parameter = Ausgang
#3. Parameter = optionaler Startwert
led1 = Pin(12, Pin.OUT,value = 0)
print(type(led1))
print(led1)

button = Pin(2,Pin.IN,Pin.PULL_UP)


while True:
  if button.value() == False:     # if pressed the push_button
      led1.value(1)             # led will turn ON
  else:                       # if push_button not pressed
      led1.value(0)             # led will turn OFF


#pull up
#taster GND -> eingang

#pull down
# taster 3v -> eingang


