from machine import Pin, SoftI2C,ADC
from time import sleep_ms

i2c  =  SoftI2C( scl=Pin(22) , sda=Pin(21))
gerate = i2c.scan()
addr = gerate[0]

wb  =  bytearray(3)

spannung = ADC(Pin(35))
spannung.atten(ADC.ATTN_11DB)
spannung.width(ADC.WIDTH_12BIT)
valueADC = spannung.read()

#print(valueADC)

def scan():
    devices = i2c.scan()
    print(devices)
    
    
def write_to():
    wb[0] =0b01100000
    spannungswert = 2056
    dac = int((spannungswert/3300)*4095)
    wb[1] = (dac >> 4)
    wb[2] = (dac << 4)
    i2c.writeto(addr , wb)

def spannung():
    print(valueADC)
    spannung_value = (valueADC / 4095)*3300
    print ( "Spannung : %.2f" %spannung_value)
    
while True:
    scan()
    write_to()
    spannung()
    sleep_ms(1500)