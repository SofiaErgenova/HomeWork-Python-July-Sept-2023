""" Возьмите 1-3 любые задачи из прошлых семинаров 
(например сериализация данных), которые вы уже решали. 
Превратите функции в методы класса, а параметры в свойства. 
Задачи должны решаться через вызов методов экземпляра """



import os
import shutil

class WorkWithFiles:
    def __init__(self, folder="", files="", new_name="", new_ext="", old_ext="", count_number="", range_list=[]):
        self.folder = folder
        self.files = files
        self.new_name = new_name
        self.new_ext = new_ext
        self.old_ext = old_ext
        self.count_number = count_number
        self.range_list = range_list

    def sort_files(self):
        """ функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. """
        dict_ext = {
            'видео': ['.mp4', '.mov'],
            'изображения': ['.heic', '.jpeg', '.png'],
            'текст': ['.txt', '.docx', '.pdf']
        }

        for file in os.listdir(self.folder):
            ext = os.path.splitext(file)[1].lower()
            for directory, ext_list in dict_ext.items():
                if ext in ext_list:
                    new_folder = os.path.join(self.folder, directory)
                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)
                    shutil.move(os.path.join(self.folder, file), new_folder)
                    break
            else:
                print(f'Файл {file} не подходит для сортировки')

    def renamed_files(self):
        """  функция группового переименования файлов """
        counter = 1
        for filename in os.listdir(self.files):
            if filename.endswith(self.old_ext):
                old_name = filename[self.range_list[0] - 1:self.range_list[1]]

                str_counter = str(counter)
                while len(str_counter) < int(self.count_number):
                    str_counter = "0" + str_counter

                final_name = old_name + self.new_name + str_counter + self.new_ext
                os.rename(os.path.join(self.files, filename), os.path.join(self.files, final_name))
                counter += 1


if __name__ == '__main__':

    directory = "/Users/sona/Desktop/Python_2/Seminar_7"
    final_name = "_new"
    digit_count = 3
    original_extension = ".txt"
    final_extension = ".new"
    range_name = [3, 6]

    work_with_files = WorkWithFiles(directory, directory, final_name, final_extension, original_extension, digit_count, range_name)
    work_with_files.renamed_files()
    work_with_files.sort_files()