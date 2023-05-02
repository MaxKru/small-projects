from time	   import sleep
from network   import WLAN, STA_IF, STAT_IDLE, STAT_CONNECTING, STAT_WRONG_PASSWORD, STAT_NO_AP_FOUND, STAT_GOT_IP
from ubinascii import hexlify
import usocket as socket
import ssl
import urequests
import umail

wlan = WLAN(STA_IF) #betrieb als teilnehmer im netzwerk
wlan.active(True)	#wlan karte aktivieren



# WLAN-Verbindung herstellen
ssid = "Phoon"
psk = "Phoon"


# Auf erfolgreiche Verbindung warten
if not wlan.isconnected():
	wlan.connect(ssid,psk)

# Auf erfolgreiche Verbindung warten
while not wlan.isconnected():
    pass



smtp = umail.SMTP('smtp.office365.com' , 587 , username='email' , password='Passwort')
smtp.to('email')
smtp.write('To: Empfängername <email> \r\n')
smtp.write('Subject: TEMP \r\n\r\n')
mailtext = 'bekommst du emails?'
smtp.write(mailtext)
smtp.send()
print("email wird gesendet")
smtp.quit()
