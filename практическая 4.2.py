a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
if a>b:
	a = a+1
	for i in range(b,a):
	    print(i,end="; ")
if b>a:
    i = int()
    for i in range (-b, -(a-1)):
        print(-i,end="; ")