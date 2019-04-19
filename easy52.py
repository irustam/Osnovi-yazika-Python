__author__ = 'Искендеров Рустам Эльдарович'

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

def lst_all_dir(dir_name = '.'):
    """
    Если нужен список не только папок, но и подпапок:
    """
    for itm in os.walk(dir_name):
        for folder in itm[1]:
            print(folder)

def lst_dir(dir_name = '.'):
    """
    Если выводим только подпапки 1-го уровня:
    """
    dirs = {}
    for key, itm in enumerate(os.listdir(dir_name)):
        if os.path.isdir(os.path.join(dir_name, itm)):
            print(f'ID {key} - Название {itm}')
            dirs[key] = itm
    return dirs

if __name__ == '__main__':
    print('Все папки, включая подпапки:')
    lst_all_dir()
    print('Папки текущей директории:')
    lst_dir()