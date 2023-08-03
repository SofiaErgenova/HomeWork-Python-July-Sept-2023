""" Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной 
расстановки ферзей в задаче выше. Проверяйте различный случайные  
варианты и выведите 4 успешных расстановки. """

import random
from queens import arrange_queens

def generate_coord(): 

    list_random = [random.randint(1, 8) for i in range(16)]
    return list_random 
 
new_list = generate_coord()

print(new_list)

print(arrange_queens(new_list))

""" new_list = [8, 5, 6, 1, 4, 8, 2, 4, 7, 7, 5, 3, 3, 6, 1, 2] // True!!!!

print(arrange_queens(new_list)) 
 """