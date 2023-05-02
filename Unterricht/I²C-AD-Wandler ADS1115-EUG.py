from machine import Pin, SoftI2C 							#Bibliothek importieren
from time import sleep_ms									#sleepfunktion importieren

i2c  =  SoftI2C( scl=Pin(22) , sda=Pin(21))					#Datenblatt ESP-32

geraet = i2c.scan()											#Adresse rausfinden


wb_A0_GND  =  bytearray(2)											#Liste mit 2*8 Bits erstellen
wb_A0_GND [0] = 0b11000010											#Erster Teil 8 Bits(Datenblatt "Default = OS(1) MUX(000) PGA(010) Mode(1) "
                                                                        #OS->bleibt so ;
wb_A0_GND [1] = 0b10000011
i2c.writeto_mem(72,0x01, wb_A0_GND)
sleep_ms(100)
int_val_A0_GND  =  int.from_bytes( i2c.readfrom_mem(72,0x00,2) , 'big')


spannung_A0_GND = int_val_A0_GND/32768*4096
#-----------------------------------------
wb_A1_GND  =  bytearray(2)											#Liste mit 2*8 Bits erstellen
wb_A1_GND [0] = 0b11010000											#Erster Teil 8 Bits(Datenblatt "Default = OS(1) MUX(000) PGA(010) Mode(1) "
                                                                        #OS->bleibt so ;
wb_A1_GND [1] = 0b10000011
i2c.writeto_mem(72,0x01, wb_A1_GND)
sleep_ms(100)
int_val_A1_GND  =  int.from_bytes( i2c.readfrom_mem(72,0x00,2) , 'big')


spannung_A1_GND = int_val_A1_GND/32768*6144


while True:
    print ("Adresse_A0_GND: %s" %geraet)								#Adresse ausgeben
    print("Dezimaler Wert_A0_GND : %i"%int_val_A0_GND)
    print("Spannung_A0_GND : %.2f mV" %spannung_A0_GND)
    print("----------------------")
    sleep_ms(1000)
    print ("Adresse_A1_GND: %s" %geraet)								#Adresse ausgeben
    print("Dezimaler Wert_A1_GND : %i"%int_val_A1_GND)
    print("Spannung_A1_GND : %.2f mV" %spannung_A1_GND)
    print("----------------------")
