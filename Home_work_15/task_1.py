""" Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров. """

import logging
import argparse 

logging.basicConfig(filename= 'logs_task_1.log',
                     filemode= 'a', 
                     encoding= 'utf-8', 
                     format= '{asctime} {levelname} {funcName}->{lineno}: {msg}',
                     style='{',
                     level= logging.INFO)
logger = logging.getLogger(__name__)


class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Нельзя создавать прямоугольник со сторонами отрицательной длины ({self.value})"


class Rectangle:
    def __init__(self, len_rec, width_rec=None):
        if len_rec < 0:
            raise NegativeValueError(len_rec)
        if width_rec is not None and width_rec < 0:
            raise NegativeValueError(width_rec)
        
        self.len_rec = len_rec
        if width_rec is None:
            width_rec = len_rec
        self.width_rec = width_rec

    def __str__(self):
        return f"Прямоугольник: длина = {self.len_rec}, ширина = {self.width_rec}"

    def perimeter_rectangle(self):
        per_rec = 2 * self.len_rec + 2 * self.width_rec
        return per_rec
    
    def square_rectangle(self):
        sq_rec = self.len_rec * self.width_rec
        return sq_rec


parser = argparse.ArgumentParser(description='Принимаем значения для прямоугольника')
parser.add_argument('-len', type=float, nargs=1, help='l - rectangle lenth')
parser.add_argument('-width', type=float, nargs=1, help='w - rectangle width', default=None)
args = parser.parse_args()


if __name__ == '__main__':
    try:
        a = Rectangle(args.len[0], args.width[0])
        logger.info(a.perimeter_rectangle())
        logger.info(a.square_rectangle())
    except NegativeValueError as e:
        logger.error(e)


# Запуск командной строкой:  python Home_work_15/task_1.py -len 5 -width 3
# Запуск командной строкой:  python Home_work_15/task_1.py -len -5 -width 3
# Запуск командной строкой:  python Home_work_15/task_1.py -len 8 -width 4