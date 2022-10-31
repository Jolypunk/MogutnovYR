print("Введите кол-во строк:")
x=int(input())
print("Введите кол-во стобцов:")
y=int(input())
k=0
s=0
a=[]
for i in range(x): 
    b=[]
    for j in range(y):
        print('Введите [',i,',',j,']' 'элемент')
        b.append(int(input()))
    a.append(b)
print("Исходный массив:")
for i in range(x):
    for j in range(y):
        print(a[i][j],end='')
    print()
for i in range(x):
    for j in range(i+1, y):
        if a[i][j] <= 0:
           continue
        if a[i][j] > 0:
            s += a[i][j]
            k+=1
print('Сумма:', s)
print('Число:', k)