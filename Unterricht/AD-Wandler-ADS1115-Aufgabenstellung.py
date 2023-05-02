from machine import Pin, SoftI2C
from time import sleep

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

geräte = i2c.scan()

adresse = geräte[0]
print(adresse)
#72
print(hex(adresse))
#0x48	

config = bytearray(2)

config[0] = 0b01000010
config[1] = 0b10000011
sleep(0.5)
i2c.writeto_mem(adresse, 0x00, config)
sleep(0.5)


while True:
	wert = int.from_bytes(i2c.readfrom_mem(adresse,0x01,2), 'big')
	print((wert/32767.0)*4096)
	sleep(1)




'''
zwei analoge quellen
dann anzeigen lassen was in den einzellnen ankommt


1. Verbindung zu i2cbus eröffnen und an variable zuweisen

2. i2c bus nach geräte abscannen
es sollte sich um das erste gerät aus der liste handeln


3. wir benötigen den ist zustand

4. ändern sie den inhalt des kinfigurationsregisters und berückstichten dabei folgende änderungen:
	mux abhängig vom verwendeten messeingang
	gain abhängig vom gewünschten messbereich
	mode 0, wennkontinurierlich
	srate abhängig vond er gewünschten daten rate
	
5. teilen sie ihr neies konfigurationswort in 2 bytes auf und speicher diese in einem bytearray mit 2 elementen

6. schreiben sie das bytearray ind as konfigurationsregister 0x01

7. die og einstellungen sind im programm nur einem notwendig und werden deswegen nich wiederholt.

8. lesen die den aktuellen messwert aus dem datenregister 0x00
	readfrom_mem liedert das ergebnis un einer liste mit 2bytes
	int.from_bytes konvertiert die lsite in einen integer

9. für die umrechnung des gelesenen digitalwertes müssen sie 15 bit berücksichtigen die referenzspannung
	richtet sich nach dem gain aus punkt 4

10. die i2cbus braucht nach oder vor jedem schreib oder lesekommando eie kleine pause. 100ms reichen aus.


'''







































