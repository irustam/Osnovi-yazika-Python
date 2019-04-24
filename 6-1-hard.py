__author__ = 'Искендеров Рустам Эльдарович'

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Worker:
    name = str()
    surname = str()
    salary = str()
    position = str()
    plan = str()
    fact = str()

    def __init__(self, worker_data):
        worker_data = worker_data.split()
        self.name = worker_data[0]
        self.surname = worker_data[1]
        self.salary = int(worker_data[2])
        self.position = worker_data[3]
        self.plan = int(worker_data[4])

    def set_fact(self, fact_data):
        self.fact = int(fact_data)

    def fullname(self):
        return self.name + ' ' + self.surname

    def count_rewards(self):
        if self.fact > self.plan:
            return round(((self.fact - self.plan) * 2 / self.plan + 1) * self.salary, 2)
        else:
            return round(self.fact * self.salary / self.plan, 2)

workers = os.path.join('data', 'workers')
hours_of = os.path.join('data', 'hours_of')

rabotnik = []
with open(workers, 'r', encoding='UTF-8') as file:
    for key, line in enumerate(file):
        if key > 0:
            rabotnik.append(Worker(line))


with open(hours_of, 'r', encoding='UTF-8') as file:
    for line in file:
        line = line.split()
        for itm in rabotnik:
            if itm.fullname() == line[0] + ' ' + line[1]:
                itm.set_fact(line[2])
                print(f'Worker: {itm.fullname()}. Reward: {itm.count_rewards()}')