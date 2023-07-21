""" Напишите программу, которая получает целое число
и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки
своего результата. """


num = int(input("Введите число: "))

print('Проверка:', hex(num))


hex_str = ''
while num > 0:
    remainder = num % 16
    if remainder == 10:
        hex_str = "a" + hex_str
    elif remainder == 11:
        hex_str = "b" + hex_str
    elif remainder == 12:
        hex_str = "c" + hex_str
    elif remainder == 13:
        hex_str = "d" + hex_str
    elif remainder == 14:
        hex_str = "e" + hex_str
    elif remainder == 15:
        hex_str = "f" + hex_str
    else:
        hex_str = str(remainder) + hex_str
    num //= 16

print("Шестнадцатеричное строковое представление:", 'Ox'+ hex_str)

