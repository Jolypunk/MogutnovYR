n=8
a=[]
for i in range(n):
    print('Введите', i ,'элемент:')
    a.append(int(input()))
for i in range(n):
    if a[i]<15:
        a[i]=a[i]*2
print(a)
        
