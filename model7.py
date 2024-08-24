# Файлы в операционной системе

import os
import time


directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        # полный путь к файлу
        filepath  = os.path.join(root, file)
        # время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # размер файла
        filesize = os.path.getsize(filepath)
        # родительская директория файла
        parent_dir = os.path.dirname(filepath)

        # Вывод информации о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
