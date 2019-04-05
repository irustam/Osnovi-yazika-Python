__author__ = 'Искендеров Рустам Эльдарович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

a = input('Enter number: ')
check = False

while check == False:
    try:
        a = int(a)
        check = True
    except:
        a = input('You entered not number. Enter number: ')

if a < 0:
    a *= -1

a = str(a)
i = 0

while i < len(a):
    print(str(i+1) + ' digit is ' + str(a[i]))
    i += 1

