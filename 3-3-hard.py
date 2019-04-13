__author__ = 'Искендеров Рустам Эльдарович'

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
ru = list(map(chr, range(ord('А'), ord('Я')+1)))

import os

fruits_file = os.path.join('data', 'fruits.txt')

"""
Первый вариант решения показался мне слишком затратным - постоянно идет обращение к файлам на дозапись. Думаю, при больших объемах он медленнее, чем вариант ниже
with open(fruits_file, 'r', encoding='UTF-8') as file:
    for line in file:
        first_symbol = line.replace('\ufeff', '')[0]
        try:
            new_fruit_file = os.path.join('data', f'fruits_{first_symbol}.txt')
            with open(new_fruit_file, 'a', encoding='UTF-8') as new_file:
                new_file.write(line)
        except:
            pass
"""
fruits_dict = {}
with open(fruits_file, 'r', encoding='UTF-8') as file:
    for line in file:
        line = line.replace('\ufeff', '')
        first_symbol = line[0]
        try:
            fruits_dict[first_symbol] += line
        except:
            fruits_dict[first_symbol] = line


for key in ru:
    if fruits_dict.get(key):
        new_fruit_file = os.path.join('data', f'fruits_{key}.txt')
        with open(new_fruit_file, 'a', encoding='UTF-8') as new_file:
            new_file.write(fruits_dict[key])
