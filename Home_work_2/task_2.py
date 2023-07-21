""" Напишите программу, которая принимает две строки вида
“a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions. """

import fractions
"""
str_1 = input("Введите первое число вида “a/b”: ")
str_2 = input("Введите второе число вида “a/b”: ")
"""
str_1 = "2/3"
str_2 = "4/5"

num_1 = int(str_1[0])
num_2 = int(str_1[2])
num_3 = int(str_2[0])
num_4 = int(str_2[2])

print(f"Умножение дробей: {num_1 * num_3}/{num_2 * num_4}")

if num_2 == num_4:
    print(f"Сложение дробей: {num_1 + num_3}/{num_2}")
else:
    print(f"Сложение дробей: {num_1 * num_4 + num_3 * num_2}/{num_2 * num_4}")

f1 = fractions.Fraction(num_1, num_2)
f2 = fractions.Fraction(num_3, num_4)

print("Проверка вычислений при помощи модуля fractions:")
print(f"Умножение дробей: {f1*f2}")
print(f"Сложение дробей: {f1+f2}")


