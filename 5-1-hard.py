__author__ = 'Искендеров Рустам Эльдарович'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import easy53
from easy51 import make_dir
from middle51 import ch_dir

print('sys.argv = ', sys.argv)
os.chdir(sys.path[0])

def print_help(_):
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def ping(_):
    print("pong")

def remove_file(file_name):
    if os.path.exists(file_name):
        if input(f'Вы уверены, что хотите удалить файл {file_name}?\ny - подтверждаю\nлюбой другой знак - отмена') == 'y':
            try:
                os.remove(file_name)
                print(f'File {file_name} removed')
            except:
                print('There is a problem with removing')
        else:
            print(f'Вы отменили удаление файла {file_name}')
    else:
        print('There is a problem with removing')

def full_dir_path(_):
    print('Текущая директория', os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": easy53.copy_file,
    "rm": remove_file,
    "cd": ch_dir,
    "ls": full_dir_path,
}

try:
    file_dir_name = sys.argv[2]
except IndexError:
    file_dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key](file_dir_name)
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
else:
    print('Не задан ключ. Укажите ключ help для получения справки')