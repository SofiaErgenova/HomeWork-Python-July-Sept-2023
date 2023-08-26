""" Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к задаче
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины. """


class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Нельзя создавать прямоугольник со сторонами отрицательной длины ({self.value})"


class Rectangle:
    def __init__(self, len_rec, width_rec=None):
        if len_rec < 0:
            raise NegativeValueError(len_rec)
        if width_rec < 0:
            raise NegativeValueError(width_rec)
        
        self.len_rec = len_rec
        if width_rec is None:
            width_rec = len_rec
        self.width_rec = width_rec

    def perimeter_rectungle(self):
        per_rec = 2 * self.len_rec + 2 * self.width_rec
        return per_rec
    
    def square_rectungle(self):
        sq_rec = self.len_rec * self.width_rec
        return sq_rec


try:
    a = Rectangle(-10)
    print(a.perimeter_rectungle())
    print(a.square_rectungle())
except NegativeValueError as e:
    print(e)

try:
    b = Rectangle(10, -5)
    print(b.perimeter_rectungle())
    print(b.square_rectungle())
except NegativeValueError as e:
    print(e)
