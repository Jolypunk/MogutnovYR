n=int(input('Введите количество элементов:\n'))
a=[]
maxa=0
for i in range(n):
    print('Введите,', i, 'элемент:')
    a.append(int(input()))
for i in range(n):
    if a[i]>maxa:
        maxa=a[i]
a.reverse()
print(a, '- массив наоборот;', maxa, '- максимальный элемент.')