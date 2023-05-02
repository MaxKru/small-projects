#dynamische typzuweisung 
z1 = 3
z2 = 5
#datentyp ausgeben
print(z1)

text = 'ET20'
print("ausgabe %s" %text)   #string ausgeben
print("ausgabe %-20s" %text)   #links buendig
print("ausgabe %20s" %text)   #rechts buendig

erg = z1 + z2
print("%i + %i = %i "%(z1,z2,erg))
erg = z1 - z2
print("%i - %i = %i "%(z1,z2,erg))
erg = z1 * z2
print("%i * %i = %05i "%(z1,z2,erg))
erg = z1 / z2
print("%i / %i = %5.1f "%(z1,z2,erg))
erg = z1 // z2
print("%i // %i = %i "%(z1,z2,erg))
erg = z1 % z2                           #Modulvision
print("%i %% %i = %i "%(z1,z2,erg))
erg = 5*10**3           # 5 mal 10^3
print("potenz %i" %erg)
erg = 5*10**(1/2)           # wurzel
print("wurzel %f" %erg)

erg = 0b1000111
print("%i" %erg)
erg = 0xfe
print("%i" %erg)

erg= 47
BinText = bin(erg)          #wandlung zu binär
print("%s" %BinText)


a = 200
b = 33
c = 50
if b > a and c == 50:
  print("b is greater than a")
elif a == b or c > 15:
  print("a and b are equal or c bigger than 15")
else:
  print("a is greater than b")


tolleliste = ['hase', 34, 55.7, 'ostern'] #datentyp liste
i = 0
while i< len(tolleliste):
  print(tolleliste[i])
  i+=1



import time

from machine import Pin

led1=Pin(15,Pin.OUT)
led2=Pin(2,Pin.OUT)
led3=Pin(4,Pin.OUT)
led4=Pin(5,Pin.OUT)
led5=Pin(18,Pin.OUT)
led6=Pin(19,Pin.OUT)

n = 1

while n > 0:
  led1.value(1)
  time.sleep(0.2)
  led1.value(0)
  led2.value(1)
  time.sleep(0.2)
  led2.value(0)
  led3.value(1)
  time.sleep(0.2)
  led3.value(0)
  led4.value(1)
  time.sleep(0.2)
  led4.value(0)
  led5.value(1)
  time.sleep(0.2)
  led5.value(0)
  led6.value(1)
  time.sleep(0.2)
  led6.value(0)
  led5.value(1)
  time.sleep(0.2)
  led5.value(0)
  led4.value(1)
  time.sleep(0.2)
  led4.value(0)
  led3.value(1)
  time.sleep(0.2)
  led3.value(0)
  led2.value(1)
  time.sleep(0.2)
  led2.value(0)





