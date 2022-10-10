n=int(input('Введите количество элементов:\n'))
a=[]
for i in range(n):
    print('Введите,', i, 'элемент:')
    a.append(int(input()))
mina=max(a)
for i in range(n):
    if a[i]<mina:
        mina=a[i]
print(mina, a.index(mina),'- индекс')