""" Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней 
квадратного уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты
 работы функции в json файл. """


from math import sqrt
import csv
import random
import json


def decor_1(func):
    def wrapper(*args):
        with open('generator.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            results = []
            for row in reader:
                a, b, c = map(float, row)
                result = func(a, b, c)
                results.append({'parameters': [a, b, c], 'result': result})
        return results
    return wrapper


def decor_2(func):
    def wrapper(*args):
        result = func(*args) 
        with open('results.json', 'w') as file:
            json.dump(result, file, indent=4)
    return wrapper


def generate_csv(rows):
    with open('generator.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['a', 'b', 'c'])
        for _ in range(rows):
            writer.writerow([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])


@decor_2
@decor_1
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c 
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x1 = -b / (2 * a)
        x2 = x1
        return x1, x2
    else:
        return None


generate_csv(100)
find_roots()
