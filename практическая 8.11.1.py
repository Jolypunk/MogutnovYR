n=int(input('Введите порядок матрицы: '))
A=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Введите [,',i,',',j,'] элемент')
        b.append(int(input()))
    A.append(b)
for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")
    print()
m=10**10
k=0
for i in range(n):
    for j in range(n):
        if A[i][j]<m:
            m=A[i][j]
            k=i
c=0
print('Результат программы: ')
for j in range(n):
    c+=A[k][j]
print(c)