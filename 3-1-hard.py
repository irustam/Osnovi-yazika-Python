__author__ = 'Искендеров Рустам Эльдарович'


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def chisla_drobi(x):
    """
    Функция возвращает числитель, знаменатель и знак числителя
    """
    drob = int(x.find('/'))

    znak_ch = 1
    if x[0] == '-':
        znak_ch = -1

    if drob >= 0:
        return abs(int(x[:drob])), int(x[drob+1:]), znak_ch
    else:
        return int(x) ** 2, abs(int(x)), znak_ch

def nod(a, b):
    """
    Функция вычисления НОД по алгоритму Евклида
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b

example = '-3 5/6 - -1 8/11'
parts = example.split()

if '-' in parts:
    znak = -1
    znak_pos = parts.index('-')
else:
    znak = 1
    znak_pos = parts.index('+')


chislitel = []
znamenatel = []
znak_chisla = []
znam = 1
for key, itm in enumerate(parts):
    if key != znak_pos:
        if ((key == 1) or (key == znak_pos + 2)) and (parts[key-1][0] == '-'):
            otric = '-'
        else:
            otric = ''

        a, b, c = chisla_drobi(otric + itm)
        chislitel.append(a)
        znamenatel.append(b)
        znam *= b

        if key > znak_pos:
            znak_chisla.append(c * znak)
        else:
            znak_chisla.append(c)

#print('Chislitel:', chislitel)
#print('Znamenatel:', znamenatel)
#print('Znak chisla:', znak_chisla)
#print('Znamenatel summ:', znam)

chislitel = sum(list(map(lambda x, y, z: int(x * z * znam / y), chislitel, znamenatel, znak_chisla)))

celoe, ostatok = divmod(abs(chislitel), znam)
#print('Verhnee chisl drobi:', ostatok)

mynod = nod(ostatok, znam)
#print('NOD:', mynod)

ostatok /= mynod
znam /= mynod

if chislitel < 0:
    celoe *= -1

if ostatok == 0 and celoe == 0:
    print(0)
elif ostatok == 0 and celoe != 0:
    print(celoe)
elif celoe:
    print(f'{celoe} {int(ostatok)}/{int(znam)}')
else:
    print(f'{int(ostatok)}/{int(znam)}')
