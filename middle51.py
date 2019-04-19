__author__ = 'Искендеров Рустам Эльдарович'

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import easy51 #Создание и удаление директорий
from easy52 import lst_dir

def ch_dir(dir_name):
    try:
        os.chdir(dir_name)
        print('Мы перешли в директорию: ', os.getcwd())
    except OSError:
        print('Ошибка в указании директории')

def choose_dir():
    dirs = lst_dir()
    try:
        dir_id = int(input('Выберите папку! Введите номер папки | другое - выход'))
        if dir_id >=0 and dirs.get(dir_id):
            return dirs.get(dir_id)
        else:
            print('Вы ввели некорректный ID папки')
            return False
    except:
        print('Вы не ввели ID папки')
        return False

def main():
    exit = False
    while not exit:
        next = input(f'Привет! Что хотите сделать?\n1 - Перейти в папку\n2 - Просмотреть содержимое текущей папки\n3 - Удалить папку\n4 - Создать папку\nлюбой другой знак - выход')
        try:
            next = int(next)
        except:
            pass

        if next == 1:
            try:
                ch_dir(choose_dir())
            except:
                pass
        elif next == 2:
            print('Содержимое текущей директории:')
            for itm in os.listdir('.'):
                print(itm)
        elif next == 3:
            try:
                easy51.remove_dir(choose_dir())
            except:
                pass
        elif next == 4:
            try:
                easy51.make_dir(input('Укажите имя новой папки'))
            except:
                pass
        else:
            print('До встреч!')
            exit = True

if __name__ == '__main__':
    main()