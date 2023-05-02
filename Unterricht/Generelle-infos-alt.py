


#dynamische typzuweisung 
z1 = 3
z2 = 5
#datentyp ausgeben
print(z1)
                                              
text = 'ET20'
print("ausgabe %s" %text)   #string ausgeben
print("ausgabe %-20s" %text)   #links buendig
print("ausgabe %20s" %text)   #rechts buendig

erg = z1 + z2
print("%i + %i = %i "%(z1,z2,erg))
erg = z1 - z2
print("%i - %i = %i "%(z1,z2,erg))
erg = z1 * z2
print("%i * %i = %05i "%(z1,z2,erg))
erg = z1 / z2
print("%i / %i = %5.1f "%(z1,z2,erg))
erg = z1 // z2
print("%i // %i = %i "%(z1,z2,erg))
erg = z1 % z2                           #Modulvision
print("%i %% %i = %i "%(z1,z2,erg))
erg = 5*10**3           # 5 mal 10^3
print("potenz %i" %erg)
erg = 5*10**(1/2)           # wurzel
print("wurzel %f" %erg)

erg = 0b1000111
print("%i" %erg)
erg = 0xfe
print("%i" %erg)

erg= 47
BinText = bin(erg)          #wandlung zu binär
print("%s" %BinText)



________________________________________________
a = 200
b = 33
c = 50
if b > a and c == 50:
  print("b is greater than a")
elif a == b or c > 15:
  print("a and b are equal or c bigger than 15")
else:
  print("a is greater than b")
________________________________________________

tolleliste = ['hase', 34, 55.7, 'ostern'] #datentyp liste
i = 0
while i< len(tolleliste):
  print(tolleliste[i])
  i+=1
_________________________________________________ ________________________________________________

#FUNKTIONEN

from time import ticks_ms

start = ticks_ms()

i=0
while i<10000:
	i+=1


stop = ticks_ms()

zeitdiff = stop - start
print("Zeit %i ms" %zeitdiff)


def fkt1():
	print("fkt1")


fkt1()




def fkt2(a,b):
	c = a+b
	return c

erg = fkt2(5,17)
print(erg)



def fkt3(a = 2, b= 3):
	c = a + b
	return c

erg = fkt3()
print(erg)

def det1(a,b):
	help = a
	a = b
	b = help
	Liste1 = [a,b]
	return Liste1


def det2(a,b):
	help = a
	a = b
	b = help
	return a,b

Liste2 = det1(56,78)
print("%i..%i" %(Liste2[0],Liste2[1]))



x,y  = det2(814,156)
print("%i.. %i" %(x,y))

________________________________________________

# Strom begrenzt auf 20mA
# Pins 32-39 nur als eingang

from machine import Pin
from time    import sleep, sleep_ms, sleep_us

#ms milisek
#us microsek

#1. Parameter = GPIO-Pin  -   general-purpose-input-output
#2. Parameter = Ausgang
#3. Parameter = optionaler Startwert
led1 = Pin(17, Pin.OUT,value = 0)
print(type(led1))
print(led1)

status = False

while True:
  led1.Value(status)    #Ausgang  = Status
  sleep(0.5)            #pause
  status = not status   #not negiert status

while True:
  led1.Value(0)   #Ausgang LOW
  sleep(0.5)      #pause
  led1.Value(1)   #Ausgang HIGH
  sleep(0.5)      #pause
  
#.

________________________________________________ ________________________________________________

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

button = Pin(2,Pin.IN,Pin.PULL_DOWN)
print(type(button))
print(button)

  
status = 2

while True:

  if button.value() == True:
    status +=1
    sleep(0.2)
    print(status)

  while status%2 == 1:
    led1.value(1)
    if button.value() == True:
      status +=1
      
    sleep(0.2)
    led1.value(0)
    if button.value() == True:
      status +=1
    sleep(0.2)
      
           


#pull up
#taster GND -> eingang

#pull down
# taster 3v -> eingang


led1 = Pin(12, Pin.OUT,value = 0)
print(type(led1))
print(led1)

button = Pin(2,Pin.IN,Pin.PULL_UP)


while True:
  if button.value() == False:     # if pressed the push_button
      led1.value(1)             # led will turn ON
  else:                       # if push_button not pressed
      led1.value(0)             # led will turn OFF
#.

z1 = 3
z2 = 5
print(z1)
print( type(z1) )
erg = z1 + z2
print("addition %i" %erg)	  


_________________________________________________ ________________________________________________


#Ein Interrupt ist ein interbrechungereignis
#Auslöser kann eine signal änderung Rising oder Falling an einem
#digitalen Eingang sein.
#Ein Interrupt hat höchste Priorität Sollte zu diesem Zeitpunkt
#eine Schleife oder ein sleep ausgeführt werden so werden diese unterbrochen
#und nach abarbeitung des interrupts fortgesetzt.

#Wenn ein Interrupt auslöst wir eine Interrupt-service-routine abgearbeitet
#dabei handelt es sich um eine funktion die sie als programmierer definieren müssen.

#Ein sleep ist übrigens in einer interrput-service-routine nicht wirksam!

#Eine weitere form des interrupts is der timer-intertupt.
#dabei wird eine interrput-service-routine entweder einmalig
#(one_shot) oder in gleichen Zeitabsänden(periodic) wiederholt
#Sie können bis zu 4 timer anlegen
#

#Beispiel

def isr_taster(pin_1):
	<do stuff>

taster = Pin(12, Pin.IN, Pin.PULL_UP)

#irq = Interrupt-Request = Unterbrechungsanforderung
#trigger  = auslöser
taster.irq(trigger=Pin.IRQ_RISING, handler=isr_taster) # wenn die flanke steigt

status = false
Whilte True:
	if taster.value()==0:
		status = not status
	if status == True
		<Blinker an>
	else
		<Blinker aus>
		
#



from machine import Pin
from time    import sleep


LED = Pin(22, Pin.OUT)

status = False



def isr_taster(Pin_nr):
  global status
  status = not status


taster = Pin(13, Pin.IN, Pin.PULL_UP)
taster.irq(trigger=Pin.IRQ_RISING, handler=isr_taster) 



while True:
	if status==True:
    LED.value(1)
    sleep(0.5)      
    LED.value(0)
    sleep(0.5)      
  else:
    LED.value(0)
  









#
from machine import Pin
from time import sleep, ticks_ms

start = ticks_ms()

led = Pin(17,Pin.OUT,value=0)
taster = Pin(16, Pin.IN, Pin.PULL_UP)


status = False

def irrtaster(Pin_nr):
    global status
    status = not status
    
taster.irq(trigger = Pin.IRQ_RISING, handler = irrtaster)

liste1 = ['a','1','b','2','c','3','d','4']

i = 0
zahl1 = 100
zahl2 = 150


while i < len(liste1):
    print(liste1[i])
    i+=1
#

def det(zahl1, zahl2):
    x = zahl1
    zahl1 = zahl2
    zahl2 = x
    return zahl1, zahl2


print(zahl1, zahl2)
zahl1,zahl2 = det(zahl1,zahl2)
print(zahl1, zahl2)






stop = ticks_ms()

diff = stop - start

print(diff)




while True:
    if status == True:
        led.value(1)
        sleep(0.25)
        led.value(0)
        sleep(0.25)
    else:
        led.value(0)
#
























































