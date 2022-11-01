P=int(input('Введите порядок матрицы: '))
A=[]
for i in range(P):
    B=[]
    for j in range(P):
        print('Введите [',i,',',j,'] элемент')
        B.append(int(input()))
    A.append(B)
print("Исходная матрица")
for i in range(P):
    for j in range(P):
        print(A[i][j],end=" ")
    print()
K=[]
for i in range(P):
    m=1
    for j in range(P):
        m*=A[j][i]
    K.append([m,i])
l=min(K,key=lambda x:x[0])
if l[1]!=P-1:
    for i in range(P):
        A[i][l[1]],A[i][l[1]+1]=A[i][l[1]+1],A[i][l[1]]
else:
    for i in range(P):
        A[i][l[1]],A[i][l[1]-1]=A[i][l[1]-1],A[i][l[1]]
print("Результат: ")
for i in range(P):
    for j in range(P):
        print(A[i][j],end=" ")
    print()