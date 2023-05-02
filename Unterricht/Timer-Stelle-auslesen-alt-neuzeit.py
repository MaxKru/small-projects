from machine import Timer, Pin
from time import ticks_ms


led = Pin(17,Pin.OUT,value=0)
taster = Pin(16,Pin.IN,Pin.PULL_UP)



altzeit = 0


timer1 = Timer(0)


def irrtaster(Pin_nr):
    global timestr, altzeit
    aktzeit = ticks_ms()
    if(aktzeit - altzeit)>200:
        if str(timer1)[-2] == "0":
            timer1.init(period=125,mode = Timer.PERIODIC,callback = irrtimer)
        else:
            timer1.deinit()
            led.value(0)
        altzeit = aktzeit

def irrtimer(Timer):
    led.value(not led.value())

taster.irq(trigger = Pin.IRQ_RISING,handler = irrtaster)








