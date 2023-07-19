""" Напишите код, который запрашивает число и 
сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым,
если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и 
чисел больше 100 тысяч.
 """


import math

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
