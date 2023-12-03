"""
Завдання:
Вам потрібно створити Python скрипт, який використовує многопоточність для пошуку файлів з конкретним розширенням
(наприклад, .txt або .jpg) в різних папках на вашому комп'ютері.

Вимоги:
1. Скрипт повинен приймати розширення файлу та список директорій для пошуку як вхідні параметри.
2. Скрипт повинен використовувати багатопотоковість для одночасного пошуку в різних директоріях.
3. Знайдені файли повинні виводитися на екран з інформацією про те, в якій папці вони були знайдені.
"""

import os
from concurrent.futures import ThreadPoolExecutor


def search_files(extension, directory):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                found_files.append(os.path.join(root, file))
    return found_files


def main(extension, directories):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(search_files, [extension] * len(directories), directories))
    for directory, files in zip(directories, results):
        print(f"Знайдено файли в папці {directory}:")
        for file in files:
            print(file)


if __name__ == "__main__":
    target_extension = input("Введіть розширення файлів (наприклад, .txt): ")
    target_directories = input("Введіть список директорій (розділіть їх комами): ").split(',')

    main(target_extension, target_directories)
