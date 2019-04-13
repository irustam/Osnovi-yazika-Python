__author__ = 'Искендеров Рустам Эльдарович'

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

workers = os.path.join('data', 'workers')
hours_of = os.path.join('data', 'hours_of')

work_hours = {}
with open(hours_of, 'r', encoding='UTF-8') as file:
    for line in file:
        rabotnik = line.split()
        work_hours[rabotnik[0] + ' ' + rabotnik[1]] = rabotnik[2]

sallary_table = {}
with open(workers, 'r', encoding='UTF-8') as file:
    for line in file:
        rabotnik = line.split()
        name = rabotnik[0] + ' ' + rabotnik[1]
        try:
            if int(work_hours[name]) > int(rabotnik[4]):
                sallary_table[name] = round(((int(work_hours[name]) - int(rabotnik[4])) * 2 / int(rabotnik[4]) + 1) * int(rabotnik[2]), 2)
            else:
                sallary_table[name] = round(int(work_hours[name]) * int(rabotnik[2]) / int(rabotnik[4]), 2)
        except:
            pass


print(sallary_table)