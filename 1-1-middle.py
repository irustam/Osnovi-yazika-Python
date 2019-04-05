__author__ = 'Искендеров Рустам Эльдарович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.


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
max_number = 0

while i < len(a):
    if max_number < int(a[i]):
        max_number = int(a[i])
    i += 1

print('Maximum is ' + str(max_number))