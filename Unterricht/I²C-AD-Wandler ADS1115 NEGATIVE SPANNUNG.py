from machine import Pin, SoftI2C
from time import sleep_ms

i2c  =  SoftI2C( scl=Pin(22) , sda=Pin(21))

gerate = i2c.scan()
addr = gerate[0]


wb  =  bytearray(2)
wb[0] = 0b10000010
wb[1] = 0b10000011

i2c.writeto_mem(addr,0x01, wb)
sleep_ms(100)



#spannnung = 0b(spannung_A0_A1)

while True:
    int_val  =  int.from_bytes(i2c.readfrom_mem(addr,0x00,2) , 'big')
    print(int_val)
    vorzeichen = int_val >>15
    print (bin(vorzeichen))
    if vorzeichen == 0:
        spannung_A0_A1 = int_val/32768*4096
        print (spannung_A0_A1)
        sleep_ms(2000)
    elif vorzeichen == 1:
        int_val -=1
        int_val ^=0b1111111111111111
        spannung_A0_A1 = int_val/32768*4096
        spannung = spannung_A0_A1*-1
        print (spannung)
        sleep_ms(2000)
    else:
        print ("x")
        sleep_ms(2000)
