""" Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех """


import csv
import random

class Text_check:
    """класс для проверки текста"""

    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.param(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Неверный формат {value}')

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name, None)

class Student:
    first_name = Text_check(str.istitle)  # дескрипторы
    first_name = Text_check(str.isalpha)
    last_name = Text_check(str.istitle)
    last_name = Text_check(str.isalpha)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    with open('study.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ученик', 'предмет', 'оценка', 'тест'])

    def generate_csv(self):
        subjects = ['математика', 'русский язык','литература','ИЗО']
        with open('study.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            for subj in subjects:
                writer.writerow([self.first_name + " " + self.last_name, subj, random.randint(2, 5), random.randint(0, 100)])
    
    def get_average_test(self, subj):
        with open('study.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            scores = [float(row[3]) for row in reader if row[1] == subj]
            if len(scores) > 0:
                return sum(scores) / float(len(scores))
            else:
                return None

    def get_average_grade(self, subj):
        with open('study.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            grades = [float(row[2]) for row in reader if row[1] == subj]
        if len(grades) > 0:
            return sum(grades) / float(len(grades))
        else:
            return None


if __name__ == '__main__':
    std_one = Student('Габриэль', 'Маркес')
    std_one.generate_csv()

    std_two = Student('Джером', 'Сэлинджер')
    std_two.generate_csv()

    std_three = Student('Эрнест', 'Хэмингуэй')
    std_three.generate_csv()

    average_test = std_one.get_average_test('математика')
    average_grade = std_one.get_average_grade('русский язык')
    print(f'По математике average_test={average_test},по русскому языку average_grade={average_grade}')

