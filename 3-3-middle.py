__author__ = 'Искендеров Рустам Эльдарович'

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def filterme(case, lst):
    newlst = []
    for item in lst:
        if case(item):
            newlst.append(item)
    return newlst

lst = [4, 23, -8, 0, -2, 10]
print(filterme(lambda x: x > 0, lst))