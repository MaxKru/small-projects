from machine import Pin, SoftI2C
from time import sleep_ms


i2c = SoftI2C(scl=Pin(22),sda=Pin(21))
gerate = i2c.scan()
addr = gerate[0]
wb = bytearray(2)

wb[0] = 0b10000010
wb[1] = 0b10000011

i2c.writeto_mem(addr,0x01, wb)
sleep_ms(200)
while True:
    int_val  =  int.from_bytes(i2c.readfrom_mem(addr, 0x00, 2) , 'big')
    sleep_ms(2000)

    if not int_val >> 15:
        print((int_val/32767.0)*4096)
    else:
        int_val ^= 0xFFFF
        int_val +=1
        print((int_val/32767.0)*4096*-1)

'''
os mux pga Mode
1  000 001 0   | 100 0011

'''



