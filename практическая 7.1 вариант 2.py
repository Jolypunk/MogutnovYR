def F(a):
    return (3**0.5/4)*a**2 #вычисление площади треугольника
def G(a):
    return (F(a))*6 #вычисление площади правильного шестиугольника
print("Программа нахождения площади правильного шестиугольника со стороной а, используя \
подпрограмму вычисления площади треугольника.")
a=int(input("Введите строну правильного шестиугольника: "))
print(G(a))
