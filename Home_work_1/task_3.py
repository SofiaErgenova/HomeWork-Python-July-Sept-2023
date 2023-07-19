""" Программа загадывает число от 0 до 1000. 
Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» 
после каждой попытки. 
Для генерации случайного числа используйте код: """

from random import randint

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

print(f'Загаданное число {num}') 
