#Joystick signal zu PWM, servo ansteuern
#Servoposition Links:1,0 ms ; Mitte: 1,5ms Rechts:2ms

from machine import ADC, PWM, Pin
from time import sleep_ms

joy = ADC(Pin(33))
joy.atten(ADC.ATTN_11DB)                    #11DB = 120mV/3130mV spannungs verstärkung
joy.width(ADC.WIDTH_11BIT)                  #11 Bit  = 2047 auflösung und werte bereich, größer -> genauer

serv = PWM(Pin(4), freq = 50)
                              #1023 = 100%, d.h --> Servopos:

#Duty Mitte :85/150
#Duty Links :29/150
#Duty Rechts:150/150

while True:
    joywert = joy.read()
    print(joywert)
    sleep_ms(50)
    
    servwert = (joywert / 2047 * 121)+29
    print(servwert)
    serv.duty(int(servwert))
'''
Zunächst wird der ADC-Wert durch 2047 geteilt, um den normalisierten ADC-Wert zu erhalten.
Der normalisierte ADC-Wert liegt zwischen 0 und 1,0.
Als nächstes wird dieser normalisierte ADC-Wert mit 121 multipliziert, um den Wertebereich auf 0-150 zu skalieren.
 Der Wert 121 ist gewählt, um den Servomotor-Duty-Cycle von 29 bis 150 zu decken.
'''

    
'''
Einige Servos verwenden eine Auflösung von 10 Bit für die Steuerung,
was bedeutet, dass die möglichen Werte für den Servopositionsbefehl zwischen 0 und 1023 liegen.
Ein Duty Cycle von 100% würde dem Wert 1023 entsprechen, während ein Duty Cycle von 0% dem Wert 0 entsprechen würde.

umrechnung Servoposition zu Pulsdauer
Servoposition Links -> puls dauer 0,566ms
dh. 0,566ms/20ms (20ms wegen der freq von 50)    ->    2,83%        29
Servoposition Rechts -> puls dauer 2,932ms
dh. 2,932ms/20ms (20ms wegen der freq von 50)    ->   14,66%       150
Servoposition Mitte -> puls dauer 1,66ms
dh. 1,66ms/20ms (20ms wegen der freq von 50)      ->   8,3%         85


Der Joystick-Wert hat einen Wertebereich von 0 bis 2047 

Der Duty-Cycle ist ein Prozentsatz der Zeit, während der ein PWM-Signal auf einen Pin aktiv ist.




'''