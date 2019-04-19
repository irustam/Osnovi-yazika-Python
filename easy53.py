__author__ = 'Искендеров Рустам Эльдарович'

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
from shutil import copy as copyme

def copy_file(file_name):
    if os.path.isfile(file_name):
        newfile = file_name + '.dupl'
        try:
            copyme(file_name, newfile)
            print(f'File {file_name} duplicated to file {newfile}')
        except:
            print(f'There is a problem with duplicatate {file_name}')
    else:
        print(f'There is a problem with duplicatate {file_name} - not exist')

if __name__ == '__main__':
    copy_file(os.path.basename(__file__))