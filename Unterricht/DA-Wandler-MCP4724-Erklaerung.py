DA- Wandler MCP4724

auflösung 12bit
die ausgegebene spannung muss in einem digitalen 12 bitwert umgerechnet werden
die versorgunfsspannung und damit die referenzspannung beträgt 3.3V

Der 12-Bit-wert muss byteweise übertragen werden. außer den hierfür 2 nötigen bytes
müssen wir ein konfigurationsbyte übertragen.

das konfigurationsbyte gibt an ob die oben errechnete spannung im EEPROM gespeichert ist oder nicht

wert nicht  im EEPROM speichern = 0b01000000
wert 	 	im EEPROM speichern = 0b01100000

Die Zerlegung des digitalen Spannungs wertes sieht wie folgt aus:
high	= unteren 4 bits entfallen
low		= die unteren 4 bits werden auf das obere halbbyte geshiftet

schreiben sie das konfigurationsbyte, das Highbyte und das Lowbyte in genau
dieser Reihenfolge in ein bytearray.


Die Kommunikation mit dem I2C bus erfolgt so:
-	zuerst legen wir eine I2C variable an, die uns mit dem Bus verbindet
	siehe softI2C

-	Lesen sie mit hilfe der funktion scan die geräteadresse aus

-	Schreiben sie mit der Funktion writeto die 3 bytes auf den Da-wandler
	<i2c-variable>.writeto(i2c-adresse, 3bytes)
	
i2c bus 

Der i2c bus verwendet eine taktleitung scl serial clock und eine datenleitung sda = serial data
die daten werden im takt der clockleitung übertragenein i2c bus kann jedooch immer nur ein byte übertragenhat man ein datenwort
welches größer ist als ein byte, dann muss dieses wort in einzelne bytes zerlegt werden
die reihenfolge der bytes beginnt beim msb ( most significant bit)
um die höherwertigen bytes für den i2c buss sichtbar zu machen muss ich sie nach rechts auf die position des niederwertigsten bytes shiften.

beim shiften werden die fehlenden stellen mit 0 bytes aufgefüllt

hier zahl = zahl << 2 so werden 2 0bits nachgeschoben
