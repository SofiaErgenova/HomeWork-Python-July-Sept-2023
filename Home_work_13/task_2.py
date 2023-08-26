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


class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Нельзя создавать треугольник со сторонами отрицательной длины ({self.value})"


while True:
    try:
        a, b, c = map(int, input('Введите значения для a, b и c через пробел: ').split())

        if a <= 0 or b <= 0 or c <= 0:
            raise NegativeValueError((a, b, c))
    except ValueError as e:
         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
    except NegativeValueError as e:
        print(f'Ваш ввод привёл к ошибке NegativeValueError: {e}')

        if (a+b) > c and (a+c) > b and (c+b) > a:
            if a == b == c:
                 print("Треугольник равносторонний")
            elif a == b or a == c or b == c:
                print("Треугольник равнобедренный")
            else:
                print("Треугольник разносторонний")
        else:
            print("Треугольник не существует")
