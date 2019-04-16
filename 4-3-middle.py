__author__ = 'Искендеров Рустам Эльдарович'

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import os
import re

numfile = os.path.join('.', 'numbers.txt')

nums = ''.join([str(random.randrange(0, 10)) for _ in range(0, 2500)])

with open(numfile, 'w', encoding='UTF-8') as file:
    try:
        file.write(nums)
    except:
        print('Some error with writing file')

if os.path.exists(numfile):
    with open(numfile, 'r', encoding='UTF-8') as file:
        try:
            numsfromfile = file.read()
        except:
            print('Some error with reading file')
else:
    print('File is not exist')

if numsfromfile:
    posled = []
    for n in range(0, 10):
        posled += re.findall(r'%s+' % n, numsfromfile)
    print(max(posled, key = len))
