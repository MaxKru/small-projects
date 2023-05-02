from machine import Pin, SoftI2C       
from time import sleep_ms        
 
i2c  =  SoftI2C( scl=Pin(22) , sda=Pin(21))

byteconf = bytearray(2)
#print(type(byteconf))
#byteconf[1] = 0b10000011
#byteconf[0] = 0b10000101
standardconfig = 0x8583
tpl = (0b100,0b101)
blank = byteconf[0] & 0b10000001

def adress():
	geraete = i2c.scan()      
	adresse = geraete[0]
	#print ("Adresse gerät: %s" %adresse)
	return adresse
	

def standardwerte():
	#print(bin(standardconfig))
	#output 0b100001011000011
	#0b1(000010110)00011
	zurücksetzen = standardconfig & 0b1000000000001111
	#print(bin(zurücksetzen))
	#output 0b1000000000000011
	
	byteconf[0] = zurücksetzen >> 8
	byteconf[1] = zurücksetzen
	#print(bin(byteconf[0]))
	
	#print(bin(byteconf[1]))
	#0b10000000
	#0b11
	return byteconf



def konfig(Userinos,Userinmux,Userinpga,Userinmod, adresse):    
	#blanken
	blank = byteconf[0] & 0b10000001
	byteconf[0] = blank
	
	
	if Userinos == "1":
		OS = 0b1
	elif Userinos == "0":
		OS = 0b0
	OS = OS << 8
	print("OS :")
	print(bin(OS))
	
	if Userinmux == "A0-GND":
		mux = 0b100
	elif Userinmux == "A1-GND":
		mux = 0b101
	mux = mux << 4
	print("mux :")
	print(bin(mux))
	
	if Userinpga == "6144":
		PGA = 0b0
	elif Userinpga == "4096":
		PGA = 0b1
	PGA = PGA >> 2
	print("PGA :")
	print(bin(PGA))
	
	if Userinmod == "1":
		MOD = 0b1
	elif Userinmod == "0":
		MOD = 0b0
	MOD = MOD >> 7
	print("MOD :")
	print(bin(MOD))
	
	print("blank :")
	print(bin(blank))	
	
	conf = blank | OS | mux | PGA | MOD
	print("conf :")
	print(bin(conf))
	
	byteconf[0] = conf
	print("byconf0 :")
	print(bin(byteconf[0]))

	i2c.writeto_mem(adresse,0x01, byteconf)
	sleep_ms(200)

def rotahilf(mux):
	conf = blank | mux
	byteconf[0] = conf
	i2c.writeto_mem(adresse,0x01, byteconf)
	sleep_ms(200)
	wert = werteinlesen(adresse)
	mv = mvcalc(wert)

def rota():
	standardconfig = 0x8583
	blank = byteconf[0] & 0b10000001
	byteconf[0] = blank
	
	for i in range(1):
		mux = tpl[i]
		mux = mux << 4
		rotahilf(mux)
	

    
def werteinlesen(adresse):
	sleep_ms(2000)
	wert =  int.from_bytes( i2c.readfrom_mem(adresse,0x00,2) , 'big')
	return wert

def mvcalc(wert):
	mv = wert/32767*4069
	print("die spannung beträgt %5.2f mV" %mv)
    
 
while True:
	adresse = adress()
	conf = standardwerte()
	neu = input("neuer messbereich oder Rotation Y/N/R")
	if neu == "Y":
		Userinos = input("messbereich auswählen os: \n")
		Userinmux = input("messbereich auswählen mux: \n")    
		Userinpga = input("messbereich auswählen pga: \n")
		Userinmod = input("messbereich auswählen mod: \n")
		konfig(Userinos,Userinmux,Userinpga,Userinmod,adresse)
	elif neu == "R":
		print("rotation")
		rota()
		
	elif neu == "N":
		print("10mal durchlaufen")
		for i in range(10):
				sleep_ms(400)
				wert = werteinlesen(adresse)
				mv = mvcalc(wert)
	
	
	wert = werteinlesen(adresse)
    
	mvcalc(wert)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    