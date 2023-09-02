"""Семинар 4 задача 6 
Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
 до конца и/или начала списка.
"""

import doctest

class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Между индексами элементов нет ({self.value})"
    

def sum_nums(lst, ind_1, ind_2):
    """
    Функция возвращает сумму чисел между между переданными индексами.
    Если индекс выходит за пределы списка, сумма считается
    до конца и/или начала списка.
    >>> sum_nums([1, 2, 3, 4, 5], 1, 4)
    7
    >>> sum_nums([1, 2, 3, 4, 5], 1, 10)
    12
    >>> sum_nums([1, 2, 3, 4, 5], -1, 4)
    10
    >>> sum_nums([1, 2, 3, 4, 5], 1, 1)
    0
    """ 

    res = 0
    if ind_1 > ind_2:
        raise NegativeValueError(res)
    elif ind_2 >= len(lst):
        return sum(lst[ind_1 + 1:])
    elif ind_1 < 0:
        return sum(lst[:ind_2])
    else:
        return sum(lst[ind_1 + 1: ind_2])


if __name__ == '__main__':
    doctest.testmod(verbose=True)
