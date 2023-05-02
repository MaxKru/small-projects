from math import pi, sin
from time import sleep_us, ticks_us


def sinus_periode(Uss = 5, Uoffset = 2.5, freq = 1, schrittweite = 2, wiederholungen = 5):
    
    Periodendauer = 1 / freq
    Wartezeit_s = Periodendauer / 360 * schrittweite
    for i in range(wiederholungen):
        for winkel in range(0,360,schrittweite):	#startwert, endwert, Schrittweite 0-359 in 1er schritten
            #t1 = ticks_us()
            sinus = sin(2*pi/360*winkel) * Uss/2 +  Uoffset        
            print('Sinus %f' %(sinus))
            #t2 = ticks_us()
            #print(t2 - t1)
            sleep_us(int(Wartezeit_s/1000)) #- (t2 - t1))
            #print('winkel %i Sinus %f Pause %f' %(winkel, sinus, Wartezeit_ms))
    
sinus_periode(5, 2.5 , 0.1, 2, 10)




'''
nachfolgende schaltung mißt jetzt 0-5V
um einen sinus im -2,5V zubekommen
kann man die Uref auf 2,5V stellen

Perioden dauer hängt von der anzahl der schritte ab hier 360 / 2 also 180 schritte

f von User gegeben

'''