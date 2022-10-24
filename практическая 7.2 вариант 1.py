def F(a):
    for i in range(n):
        if n>15:
            return "Первый массив содержит больше 15 элементов."
    else:
        return sum(a)
def G(a):
    if F(a)!=sum(a):
        return "ошибка"
    else:
        return sum(a)/n
print("Вычисление сумммы и среднее арифметического чисел в массиве.")
print("Введите кол-во элементов первого массива:")
a=[]
b=[]
c=[]
n=int(input())
for i in range(n):
    print("Введите", i, "элемент:")
    a.append(int(input()))
print("Сумма чисел в массиве -", F(a))
print("Cреднее арифметическое чисел в массиве -", G(a))
def F(b):
    for i in range(k):
        if k>15:
            return "Второй массив содержит больше 15 элементов."
    else:
        return sum(b)
def G(b):
    if F(b)!=sum(b):
        return "ошибка"
    else:
        return sum(b)/k
print("Введите кол-во элементов второго массива:")
k=int(input())
for i in range(k):
    print("Введите", i, "элемент:")
    b.append(int(input()))
print("Сумма чисел в массиве -", F(b))
print("Cреднее арифметическое чисел в массиве -", G(b))
def F(c):
    for i in range(u):
        if u>15:
            return "Третий массив содержит больше 15 элементов."
    else:
        return sum(c)
def G(c):
    if F(c)!=sum(c):
        return "ошибка."
    else:
        return sum(c)/u
print("Введите кол-во элементов третьего массива:")
u=int(input())
for i in range(u):
    print("Введите", i, "элемент:")
    c.append(int(input()))
print("Сумма чисел в массиве -", F(c))
print("Cреднее арифметическое чисел в массиве -", G(c))