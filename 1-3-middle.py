__author__ = 'Искендеров Рустам Эльдарович'

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = input('Enter value A: ')
b = input('Enter value B: ')
c = input('Enter value C: ')

check = False

while check == False:
    try:
        a = float(a)
        check = True
    except:
        a = input('You entered A not number. Enter number: ')

check = False

while check == False:
    try:
        b = float(b)
        check = True
    except:
        b = input('You entered B not number. Enter number: ')

check = False

while check == False:
    try:
        c = float(c)
        check = True
    except:
        c = input('You entered C not number. Enter number: ')

try:
    koren_dscr = math.sqrt(b ** 2 - 4 * a * c)
except:
    koren_dscr = -1

if b == 0 and c == 0 and a != 0:
    print('Only one X is 0')
elif a == 0 and b != 0:
    x1 = -c / b
    print('Only one X is ' + str(x1))
elif b == 0 and a == 0:
    print('There is no solution')
elif koren_dscr >= 0:
    x1 = (-b + koren_dscr) / (2 * a)
    x2 = (-b - koren_dscr) / (2 * a)
    print('X1 is ' + str(x1) + ' X2 is ' + str(x2))
else:
    print('There is no solution')