
""" Треугольник существует только тогда,
когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны
 с суммой двух других.
 Если хотя бы в одном случае отрезок окажется
 больше суммы двух других, то треугольника с такими
 сторонами не существует.
 Отдельно сообщить является ли треугольник разносторонним,
  равнобедренным или равносторонним. """


# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
#
# if (a+b) > c and (a+c) > b and (c+b) > a:
#     if a == b == c:
#         print("Треугольник равносторонний")
#     elif a == b or a == c or b == c:
#         print("Треугольник равнобедренный")
#     else:
#         print("Треугольник разносторонний")
# else:
#     print("Треугольник не существует")


""" 3. Напишите код, который запрашивает число и 
сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым,
если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и 
чисел больше 100 тысяч.
 """


""" import math

min_limit = 0
max_limit = 100000

while True:
    print('Введите число между', min_limit, 'и', max_limit,': ')
    num = int(input())
    if num > min_limit and num < max_limit:
        break
    else:
        print("Неверное значение")

if num == 1:
    print('Это число не является ни простым, ни составным')
else:
    is_prime = True
    sqrt_num = math.isqrt(num)
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print('Это число является простым')
    else:
        print('Это число является составным')
 """

""" Программа загадывает число от 0 до 1000. 
Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» 
после каждой попытки. 
Для генерации случайного числа используйте код: """

""" from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
user_num = print("Программа загадала число от 0 до 1000. Необходимо угадать число за 10 попыток. ")
attempt = 10

while attempt > 0:
      user_num = int(input("Введите число: "))
      if num == user_num:
        print("Вы угадали!")
        break
      else:
        attempt -= 1
        if num > user_num:
          print(f'Не угадали! Это число больше. Осталось попыток {attempt}')
        else: 
          print(f'Не угадали! Это число меньше. Осталось попыток {attempt}')
print(f'Загаданное число {num}')  """



""" Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
 """

import math

a = 5
b = -10
c = -400

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
elif d == 0:
    x1 = -b/(2*a)
    x2 = x1
else:
    x1 = None
    x2 = None

print("x1 =", x1)
print("x2 =", x2)

