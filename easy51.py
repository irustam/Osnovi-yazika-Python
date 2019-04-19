__author__ = 'Искендеров Рустам Эльдарович'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

def make_dir(dir_name):
    """
    Создание папки с указанным именем
    """
    if not dir_name:
        print("Необходимо указать имя директории")
        return False
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
        return True
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
        return False

def remove_dir(dir_name):
    """
    Удаление указанной папки
    """
    if not dir_name:
        print("Необходимо указать имя директории")
        return False
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir_name))
        return True
    except OSError:
        print('директория {} не пуста'.format(dir_name))
        return False
    except FileExistsError:
        print('директория {} не существует'.format(dir_name))
        return False

if __name__ == '__main__':
    for i in range(1, 10):
        make_dir('dir' + str(i))
    for i in range(1, 10):
        remove_dir('dir' + str(i))