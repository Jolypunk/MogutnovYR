import math
def F(n):
	if n=="Треугольник":
		return (a*b/2)
	if n=="Параллелограмм":
		return (a*h)
	if n=="Круг":
		return (2*math.pi*r**2)
print("Программа для вычисления площади треугольника,\
параллелограмма, круга.")
print("Введите с большой буквы название геометрической фигуры для вычисления площади:")
n=input()
if n=="Треугольник":
	a=float(input("Введите длину стороны: "))
	b=float(input("Введите длину основания: "))
	print(F(n))
elif n=="Параллелограмм":
	a=float(input("Введите длину стороны основания: "))
	h=float(input("Введите высоту: "))
	print(F(n))
elif n=="Круг":
	r=float(input("Введите радиус: "))
	print(F(n))
else:
	print("Нет информации о фигуре или она не правильно введена.")