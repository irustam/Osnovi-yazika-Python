__author__ = 'Искендеров Рустам Эльдарович'

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

# Получаем кол-во элементов
check = False

while not check:
    itter = input('How much generate? ')
    try:
        itter = int(itter)
        check = True
        if itter <= 0:
            check = False
    except:
        print('You entered not valid number')
################# Получили

mylist = []
i = 0
while i < itter:
    mylist.append(random.randint(-100,100))
    i += 1
print(mylist)