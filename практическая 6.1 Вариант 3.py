n=int(input('Введите количество элементов:\n'))
D=[] #массив всех чисел
for i in range(n):
    print('Введите,', i, 'элемент:')
    D.append(int(input()))
sumn=0 #сумма чисел с нечёт индексом
for i in range(n):
    if D.index(D[i])%2==1:
        sumn+=D[i]
print(D, sumn, '- сумма чисел с нечётным индексом.')