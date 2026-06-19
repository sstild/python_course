# a = float(input("Enter a:"))
# b = float(input("Enter b:"))
# c = float(input("Enter c:"))
# p = a+b+c
# print("perimeter", p)

d, e, f = map(float,input("Введите длины сторон треуольника через пробел:").split())
print(f"d={d}, e={e}, f={f}")
perimetr = d+e+f
print(f"Периметр треугольника = {perimetr}")


