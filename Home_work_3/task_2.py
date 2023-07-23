"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
"""

lst = [4, 4, 5, 5, 3, 3, 1, 5, 1]
print(lst)
print(list(set(lst)))

new_lst = []
for el in lst:
    if el not in new_lst:
        new_lst.append(el)
print(sorted(new_lst, reverse = False))