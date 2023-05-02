from time  import sleep
from umail import SMTP
from machine import Pin, SPI
#from Dateiname ohne Endung import Funktionsname

# Pin-Objekt für Chip-Select erstellen
cs = Pin(5, Pin.OUT)

# SPI-Objekt erstellen
spi = SPI(1, baudrate	=1000000, polarity=1, phase=1, bits=8, firstbit=SPI.MSB,
          sck=Pin(18), miso=Pin(19))

# Bytearray für Temperaturdaten erstellen
data = bytearray(2)

#smtp = send message transfer protocol
def MailSenden():
#oder           'outlook.office365.com'
#587 = Port
    smtp = SMTP('smtp.office365.com' , 587, username='email' , password='Passwort')
    #smtp = SMTP('smtp.gmail.com' , 587 , username='email' , password='Passwort')
    smtp.to('email')
    smtp.write('To: Empfängername <email> \r\n')
    smtp.write('Subject: Titel \r\n\r\n')
    mailtext = 'Bei mir zuhause ist es grade %.2f C warm.' %temp_c
    smtp.write(mailtext)
    smtp.send()
    print("email wird gesendet")
    smtp.quit()




def Connect_WiFi(ssid='Phoon' , pswd='williwonka' , adressdaten=() ):
	from network   import WLAN, STA_IF, STAT_IDLE, STAT_CONNECTING, STAT_WRONG_PASSWORD, STAT_NO_AP_FOUND, STAT_GOT_IP
	from ubinascii import hexlify

	meinNetz = WLAN(STA_IF)				#Netzwerkobjekt im Stationsmodus
	meinNetz.active(False)				#Netzwerkkarte deaktivieren
	sleep(0.5)
	meinNetz.active(True)				#Netzwerkkarte aktivieren
	sleep(0.5)
	
	if len(adressdaten)==4:				#statische Adressdaten verwenden
		meinNetz.ifconfig(adressdaten)
		sleep(0.5)

	gefundeneNetze = meinNetz.scan()	#WLAN-Netze scannen
	print(gefundeneNetze)
	for netz in gefundeneNetze:
		wlan_netz = netz[0].decode('utf-8') #Bytes aus Tuple in String wandeln
		print('SSID %-25s  Kanal %2i  RSSI %i db' %(wlan_netz,netz[2], netz[3]))

	if not meinNetz.isconnected():
		meinNetz.connect(ssid, pswd)
		sleep(3)
		i=0
		while i<10:
			wlan_status = meinNetz.status()
			if   wlan_status==STAT_IDLE:
				print('there is no connection or activity')
			elif wlan_status==STAT_CONNECTING:
				print('connection is in progress')
			elif wlan_status==STAT_WRONG_PASSWORD:
				print('network connection failed due to an incorrect network key')
			elif wlan_status==STAT_NO_AP_FOUND:
				print('network connection failed because no access point replied to the connection request')
#			elif wlan_status==STAT_CONNECT_FAIL:
#				print('network connection failed due to another reason')
			elif wlan_status==STAT_GOT_IP:
				print('network is successfully connected and the IP is obtained')
				break
			i+=1
			sleep(1)

	mac_b = meinNetz.config('mac')
	mac_s = hexlify(mac_b, ':').decode('utf-8').upper()
	print(mac_s)
	
	if meinNetz.status()==STAT_GOT_IP:
		print('IP          ', meinNetz.ifconfig()[0])
		print('SNM         ', meinNetz.ifconfig()[1])
		print('GW          ', meinNetz.ifconfig()[2])
		print('DNS         ', meinNetz.ifconfig()[3])
		print(meinNetz.ifconfig())
		return meinNetz.ifconfig()[0]
	else:
		return False





ret=False
while ret==False:
#	ret = Connect_WiFi()
	ret = Connect_WiFi('ssid' , 'pw')
#Aufruf mit statischen Adressdaten                  IP           SNM          GW            DNS
	#ret = Connect_WiFi('ssid , 'pw' , ('10.1.1.1','255.0.0.0','10.6.109.10','10.6.109.10'))

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
    sleep(1)
    MailSenden()