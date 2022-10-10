n=int(input('Введите количество элементов:\n'))
a=[] #массив всех чисел
for i in range(n):
    print('Введите,', i, 'элемент:')
    a.append(int(input()))
pol=[] #массив положительных чисел
ot=[] #массив отрицательных чисел
for i in range(n):
    if a[i]>=0:
        pol.append(a[i])
    else:
        ot.append(a[i])
print(pol, ot)