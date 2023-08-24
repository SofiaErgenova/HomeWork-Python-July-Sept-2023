""" Добавьте ко всем задачам строки документации
и методы вывода информации на печать. """


from datetime import datetime

class MyStr(str):
    """
    MyStr - class, наследует все возможности класса str
    также имеет дополнительные атрибуты
    """

    def __new__(cls, value, author_name):
        """
        Создает экземпляр класса с дополнительными атрибутами
        value: Переданная строка
        author_name: имя автора-создателя
        creation_time = datetime.datetime.now() - время создания
        """

        my_srt = super().__new__(cls, value)
        my_srt.author_name = author_name
        # my_srt.creation_time = time.time()
        my_srt.creation_time = datetime.now()
        return my_srt
    
class Archive:
    """
    класс Archive хранит свойства:
    число и строку, а также list-архивы предыдущих экземпляров класса.
    При нового экземпляра класса, старые данные из ранее созданных экземпляров 
    сохраняются в два списковархивов
    """

    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None

    def __init__(self, num, new_str):
        self.num = num
        self.new_str = new_str

        if Archive.last_num is not None:
            Archive.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.strs_archive.append(Archive.last_str)

        Archive.last_num = num
        Archive.last_str = new_str  


class Rectangle:
    """Класс для работы с прямогульником"""

    def __init__(self, side_a, side_b=0):
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        """Получение периметра"""
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        """Получение площади"""
        return self.side_a * self.side_b

    def __add__(self, other):
        """Сложение прямоугольников"""
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """Вычитание прямоугольников"""
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  
        """Проверка на равенство  прямоугольников"""
        return self.get_area() == other.get_area()

    def __ne__(self, other):  
        """Проверка на неравенство прямоугольников"""
        return self.get_area() != other.get_area()

    def __gt__(self, other):  
        """Первый прямоугольник больше второго прямоугольника"""
        return self.get_area() > other.get_area()

    def __ge__(self, other):  
        """Первый прямоугольник больше или равен второму прямоугольнику"""
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  
        """Первый прямоугольник меньше второго прямоугольника"""
        return self.get_area() < other.get_area()

    def __le__(self, other):  
        """Первый прямоугольник меньше или равен второму прямоугольнику"""
        return self.get_area() <= other.get_area()


print(f'Документация класса: {MyStr.__doc__ = }')
print(f'Документация метода: {MyStr.__new__.__doc__}')

print(f'Документация класса: {Archive.__doc__ = }')


print(f'Документация класса: {Rectangle.__doc__ = }')
print(f'Документация метода: {Rectangle.get_perimeter.__doc__}')

