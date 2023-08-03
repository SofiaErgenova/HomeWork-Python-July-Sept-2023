""" Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число 
от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните
истину, а если бьют - ложь.
"""



def arrange_queens(coordinates):

    first_values = [coordinates[i] for i in range(len(coordinates)) if i % 2 == 0]
    
    second_values = [coordinates[j] for j in range(len(coordinates)) if j % 2 != 0]

    if len(first_values) != len(set(first_values)):
        return False
    else:
        if len(second_values) != len(set(second_values)):
            return False
        else: 
            for i in range(len(first_values)):
                for j in range(i+1, len(second_values)):
                    if abs(first_values[i] - first_values[j]) == abs(second_values[i] - second_values[j]):
                        return False
                    else:
                        return True
 
