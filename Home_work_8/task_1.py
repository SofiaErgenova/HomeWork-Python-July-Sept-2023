""" Напишите функцию, которая получает на вход директорию и 
рекурсивно обходит её и все вложенные директории. 
Результаты обхода 
сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, 
а для директорий размер файлов в ней 
с учётом всех вложенных файлов и директорий.
 """

import os
import json
import csv
import pickle

def directory_structure(directory):

    structure = []

    for dir_path, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:

            dir_size = 0
            for dirpath, dirnames, filenames in os.walk(os.path.join(dir_path, dirname)):
                for file in filenames:
                    fp = os.path.join(dirpath, file)
                    dir_size += os.path.getsize(fp)

            structure.append({
                'path': os.path.join(dir_path, dirname),
                'type': 'directory',
                'size': dir_size
            })
        
        for filename in filenames:
            file_path = os.path.join(dir_path, filename)
            file_size = os.path.getsize(file_path)
            structure.append({
                'path': file_path,
                'type': 'file',
                'size': file_size
            })

    with open('structure.json', 'w', encoding="utf-8") as file:
        json.dump(structure, file)

    with open('structure.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['path', 'type', 'size'])
        for struc in structure:
            writer.writerow([struc['path'], struc['type'], struc['size']])

    with open('structure.pickle', 'wb') as file:
        pickle.dump(structure, file)

directory_structure('/Users/sona/Desktop/Python_2/Seminar_3')



