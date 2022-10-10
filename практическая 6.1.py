n=int(input('Введите количество элементов:\n'))
a=[]
sr=0
for i in range(n):
    print('Введите,', i, 'элемент:')
    a.append(float(input()))
for i in range(n):
    sr=sr+a[i]
sr=sr/n
for i in range(n):
    if a[i]<1:
        a[i]=sr
print(a)
