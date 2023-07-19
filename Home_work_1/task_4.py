""" Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
 """

import math

a = 5
b = -10
c = -400

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d))/(2 * a)
    x2 = (-b - math.sqrt(d))/(2 *a )
elif d == 0:
    x1 = -b/(2 * a)
    x2 = x1
else:
    x1 = None
    x2 = None

print("x1 =", x1)
print("x2 =", x2)

