"""
Напишите функцию принимающую на вход только ключевые параметры 
и возвращающую словарь, где ключ — значение переданного аргумента, 
а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
"""


def create_dict(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        if isinstance(hash(key), int):
            key = str(key)
        dict[value] = key
    return dict


new_dict = create_dict(one=1, two=2, three=3, four=4, five=5)
print(new_dict)
