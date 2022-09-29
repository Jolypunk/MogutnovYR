print('Программа по нахождению минимального числа.')
print('Введите 3 переменные:')
a=int(input())
b=int(input())
c=int(input())
z=0
if a<b and a<c:
    z=a
elif b<c and b<a:
    z=b
else:
    z=c
print('Минимальное число:',z)