import time
from machine import Pin, SPI


# Pin-Objekt für Chip-Select erstellen
cs = Pin(5, Pin.OUT, value = 1)

# SPI-Objekt erstellen
spi = SPI(1, baudrate	=1000000, polarity=1, phase=1, bits=8, firstbit=SPI.MSB,
          sck=Pin(18), miso=Pin(19))

#firstbit = SPI.MSB
'''
mosi brauchen wa nich weil wegen der max empfängt nix


'''

# Bytearray für Temperaturdaten erstellen
data = bytearray(2)

while True:
    # Chip auswählen
    cs.value(0)

    # Temperaturdaten in bytearray lesen
    spi.readinto(data)

    # Chip abwählen
    cs.value(1)

    # Bytes kombinieren, um Temperaturwert zu erhalten
    Tread = (data[0] << 8) | data[1]
    
    temp_raw = Tread >> 3
    print(bin(Tread))
    print(bin(temp_raw))
    
    # Negative Temperaturwerte behandeln
    # zwöfte bit anschauen
    if temp_raw & 0x1000:
        temp_raw = ~temp_raw + 1
        #temp_raw ^= 0xffff
        #temp_raw += 1
    
    

    # Tatsächlichen Temperaturwert berechnen
    temp_c = temp_raw * 0.25

    print("Temperatur: %.2f C" %temp_c)

    # 1 Sekunden warten
    time.sleep(1)
