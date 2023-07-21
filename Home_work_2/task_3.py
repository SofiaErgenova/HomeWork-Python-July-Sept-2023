""" Напишите
программу, которая решает квадратные
уравнения даже если дискриминант отрицательный.
 Используйте комплексные числа для
извлечения квадратного корня.
"""

import math
import cmath

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d))/(2 * a)
    x2 = (-b - math.sqrt(d))/(2 * a)
elif d == 0:
    x1 = -b/(2 * a)
    x2 = x1
else:
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)

print("x1 =", x1)
print("x2 =", x2)
