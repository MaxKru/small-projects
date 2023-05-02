from machine import Pin
from time import sleep, ticks_ms

start = ticks_ms()

led = Pin(17,Pin.OUT,value=0)
taster = Pin(16, Pin.IN, Pin.PULL_UP)


status = False


altzeit = 0

def irrtaster(Pin_nr):
    global status, altzeit
    aktzeit = ticks_ms()
    if (altzeit - aktzeit)>100:
        status = not status
    altzeit = aktzeit




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


