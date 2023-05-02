'''

vorzeichen stelle anzeigenlassen:

vorwärtz rückwärtz rechnen

umwandeln von positiv zu negativ

0001 0001			17
bits invertieren
1110 1110
+1
1110 1111			-17

0^1 = 1
1^1 = 0

zahl  =  0b00010001
zahl = 17

0001 0001 & (1<<7) -> 0

1110 1111 & (1<<7) -> !0






'''
#werte invertieren

wert = 0b1010

print(wert)

print(~wert+1)

wert2 = ~wert+1

print(bin(wert2))
print(wert2)

