"""Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение."""


import os
def renamed_files(files, new_name, new_ext, old_ext, count_number, range_list):
    counter = 1

    for filename in os.listdir(files):
        if filename.endswith(old_ext):
            old_name = filename[range_list[0] - 1:range_list[1]]

            str_counter = str(counter)
            while len(str_counter) < int(count_number):
                str_counter = "0" + str_counter

            final_name = old_name + new_name + str_counter + new_ext
            os.rename(os.path.join(files, filename), os.path.join(files, final_name))
            counter += 1

directory = "/Users/sona/Desktop/Python_2/Seminar_7"
final_name = "_new"
digit_count = 3
original_extension = ".txt"
final_extension = ".new"
range_name = [3, 6]

renamed_files(directory, final_name, final_extension, original_extension, digit_count, range_name)