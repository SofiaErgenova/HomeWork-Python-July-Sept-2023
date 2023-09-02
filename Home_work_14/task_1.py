""" Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях.
Напишите к ним тесты.
2-5 тестов на задачу в трёх вариантах:
○ doctest,
○ unittest,
○ pytest.  """

"""  Задание No1 Семинар 10
📌 Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие длину окружности
 и её площадь.
     """

import doctest
from math import pi

class Circle:
    """
    Класс создания окружности по радиусу для вычисления длины окружности
 и её площади.
    >>> Circle.length_circle(Circle(5))
    31.41592653589793
    >>> Circle.square_circle(Circle(5))
    78.53981633974483
    """

    def __init__(self, radius):
        self.radius = radius

    def length_circle(self):
        len_circle = 2 * pi * self.radius
        return len_circle
    
    def square_circle(self):
        sq_circle = pi * self.radius ** 2
        return sq_circle


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)