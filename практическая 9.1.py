a=[]
k=0
s=0
with open('E:\python\практическая 9\\практическая 9.1.1.txt','r') as f:
    for line in f.readlines():
        b=line.replace('\n','').split()
        for i in range(len(b)):
            b[i]=int(b[i])
        a.append(b)
    print(a)
    print('Исходный:')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],' ',end='')
    print()
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i][j] <= 0:
            continue
        if a[i][j] > 0:
            s += a[i][j]
            k+=1
print('Сумма:', s)
print('Число:', k)
with open('E:\python\практическая 9\\практическая 9.1.2.txt','w') as t:
    t.write('Summa:'+ " " + str(s) + '\n')
    t.write('Chislo:'+ " " + str(k) + '\n')