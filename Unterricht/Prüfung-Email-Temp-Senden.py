from umail import SMTP
from network import WLAN, STA_IF, STAT_IDLE, STAT_CONNECTING, STAT_WRONG_PASSWORD, STAT_NO_AP_FOUND, STAT_GOT_IP
from time import sleep
from machine import Pin, SPI

cs = Pin(5, Pin.OUT, value=1)

Max6675 = SPI(1,baudrate = 1000000, polarity = 0, phase = 0, bits= 8, firstbit = SPI.MSB, sck=Pin(18), miso=Pin(19))
data = bytearray(2)


def Wlan():
    print("wlan wird verbunden")
    
    SSID = "CMCC-9kCD"
    PSW = "12345678"

    SSID = "Phoon"
    PSW = "williwonka"
    

    wlan = WLAN(STA_IF)
    wlan.active(True)

    wlan.connect(SSID, PSW)

    sleep(1)

    while not wlan.isconnected():
        pass

    print("wlan verbunden")

def emailschreiben(temp):
    email = SMTP('smtp.office365.com', 587, username='email', password='passwort')
    email.to('email')
    email.write('To: Empfängername <email>' + "\r\n")
    email.write('Subject: Warnung TEMP \r\n\r\n')
    Emailtxt = "Temperatur ist zu hoch! temp : %.2f C \r\n" %temp
    email.write(Emailtxt)
    email.send()
    print("email wurde gesendet")
    email.quit()
    

def temperaturlesen():
    
    cs.value(0)
    sleep(0.1)
    Max6675.readinto(data)
    sleep(0.1)
    cs.value(1)
    
    Tread = data[0] << 8 | data[1]
    
    Tempraw = Tread >> 3
    
    Tempgrad = Tempraw * 0.25
    return Tempgrad
        

Wlan()

while True:
    
    temp = temperaturlesen()
    sleep(1)
    
    if temp > 30:
        emailschreiben(temp)
    else:
        print("temp %.2f ist noch unter 30°C" %temp)
    





















