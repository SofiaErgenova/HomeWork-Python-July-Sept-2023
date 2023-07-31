"""
Напишите функцию, которая принимает на вход строку — 
абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: 
путь, имя файла, расширение файла.
"""

def func(str):
    
    *path, name_extension = str.split('/')
    name_file, extension = name_extension.split('.')
    return path, name_file, extension


link = 'Users/sonia/server/data.py'
print(func(link))

