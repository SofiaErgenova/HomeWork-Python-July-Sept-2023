"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

"""

import os
import shutil

def sort_files(folder):
    dict_ext = {
        'видео': ['.mp4', '.mov'],
        'изображения': ['.heic', '.jpeg', '.png'],
        'текст': ['.txt', '.docx', '.pdf']
    }

    for file in os.listdir(folder):
            ext = os.path.splitext(file)[1].lower()
            for directory, ext_list in dict_ext.items():
                if ext in ext_list:
                    new_folder = os.path.join(folder, directory)
                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)
                    shutil.move(os.path.join(folder, file), new_folder)
                    break
            else:
                print(f'Файл {file} не подходит для сортировки')


sort_files('/Users/sona/Desktop/may_2023')