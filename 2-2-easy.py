__author__ = 'Искендеров Рустам Эльдарович'

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random

# Получаем кол-во элементов в списке и генерируем список
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

lst1 = []
i = 0
while i < itter:
    lst1.append(random.randint(0,50))
    i += 1

lst2 = []
i = 0
while i < itter:
    lst2.append(random.randint(0,50))
    i += 1
################# Получили


print(f'First list {lst1}')
print(f'Second list {lst2}')


# Удаление повторов
for itm in lst2:
    i = lst1.count(itm)
    while i > 0:
        lst1.remove(itm)
        i -= 1
################# Удалили

print(f'New first list {lst1}')