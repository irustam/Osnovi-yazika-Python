__author__ = 'Искендеров Рустам Эльдарович'

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random

# Получаем кол-во элементов и генерируем список
check = False

while not check:
    itter = input('How much should numbers be in list? ')
    try:
        itter = int(itter)
        check = True
        if itter <= 0:
            check = False
    except:
        print('You entered not valid number')

lst = []
i = 0
while i < itter:
    lst.append(random.randint(-100,100))
    i += 1
################# Получили

newlst = []

for itm in lst:
    krt = int(itm) % 2
    if krt == 0:
        newlst.append(int(itm) / 4)
    else:
        newlst.append(int(itm) * 2)

print(f'Your list {lst}')
print(f'New list {newlst}')