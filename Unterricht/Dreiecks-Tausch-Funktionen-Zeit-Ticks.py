from time import ticks_ms

start = ticks_ms()

i=0
while i<10000:
	i+=1


stop = ticks_ms()

zeitdiff = stop - start
print("Zeit %i ms" %zeitdiff)


def fkt1():
	print("fkt1")


fkt1()




def fkt2(a,b):
	c = a+b
	return c

erg = fkt2(5,17)
print(erg)



def fkt3(a = 2, b= 3):
	c = a + b
	return c

erg = fkt3()
print(erg)

def det1(a,b):
	help = a
	a = b
	b = help
	Liste1 = [a,b]
	return Liste1


def det2(a,b):
	help = a
	a = b
	b = help
	return a,b

Liste2 = det1(56,78)
print("%i..%i" %(Liste2[0],Liste2[1]))



x,y  = det2(814,156)
print("%i.. %i" %(x,y))





























