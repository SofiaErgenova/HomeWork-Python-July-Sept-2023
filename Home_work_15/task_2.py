""" ДЗ 1 Задача 1. Треугольник существует только тогда,
когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны
 с суммой двух других.
 Если хотя бы в одном случае отрезок окажется
 больше суммы двух других, то треугольника с такими
 сторонами не существует.
 Отдельно сообщить является ли треугольник разносторонним,
  равнобедренным или равносторонним. """

import logging
import argparse

logging.basicConfig(filename='logs_task_2.log',
                     filemode='a',
                     encoding='utf-8',
                     format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
                     style='{',
                     level=logging.INFO)
logger = logging.getLogger(__name__)


class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Нельзя создавать треугольник со сторонами отрицательной длины ({self.value})"


parser = argparse.ArgumentParser(description='Принимаем значения сторон для треугольника')
parser.add_argument('-a', type=float, nargs=1, help='а - сторона треугольника')
parser.add_argument('-b', type=float, nargs=1, help='в - сторона треугольника')
parser.add_argument('-c', type=float, nargs=1, help='с - сторона треугольника')
args = parser.parse_args()

if args.a or args.b or args.c:
    try:
        a, b, c = args.a[0], args.b[0], args.c[0]

        if a <= 0 or b <= 0 or c <= 0:
            raise NegativeValueError((a, b, c))
            
        if (a+b) > c and (a+c) > b and (c+b) > a:
            if a == b == c:
                logger.info("Треугольник равносторонний")
            elif a == b or a == c or b == c:
                logger.info("Треугольник равнобедренный")
            else:
                logger.info("Треугольник разносторонний")
        else:
            logger.info("Треугольник не существует")
    except ValueError as e:
        logger.error(str(e))
    except NegativeValueError as e:
        logger.error(str(e))



# Запуск командной строкой:  python Home_work_15/task_2.py -a 5 -b 3 -c 8
# Запуск командной строкой:  python Home_work_15/task_2.py -a 6 -b 3 -c 8
# Запуск командной строкой:  python Home_work_15/task_2.py -a 3 -b 3 -c 3
# Запуск командной строкой:  python Home_work_15/task_2.py -a 4 -b 3 -c 3
# Запуск командной строкой:  python Home_work_15/task_2.py -a -4 -b 3 -c 3