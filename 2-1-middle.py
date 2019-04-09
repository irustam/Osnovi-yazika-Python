__author__ = 'Искендеров Рустам Эльдарович'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

mylist = [2, -5, 8, 9, -25, 25, 4]
sqrlist = []

for itm in mylist:
    try:
        sqr_itm = math.sqrt(itm)

        if sqr_itm % int(sqr_itm) == 0:
            sqrlist.append(int(math.sqrt(itm)))
    except:
        pass

print(sqrlist)