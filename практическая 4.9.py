a = b = 1
x = 2
n = int(input('Введите кол-во чисел из ряда Фибоначчи: '))
for i in range(2, n):
    a, b = b, a + b
    x += b
print(x)