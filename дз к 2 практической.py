import math
x=int(input("Введите число x: "))
y=int(input("Введите число y: "))
z=float(((1*math.sin(x)-2*math.pi)/(math.fabs(math.cos(y))+math.sqrt(x)))*math.pow(math.e,y))
print("z={0:.2}".format(z))
