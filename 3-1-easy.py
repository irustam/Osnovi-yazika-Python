__author__ = 'Искендеров Рустам Эльдарович'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    celoe, des = divmod(number, 1)

    ch1 = int(str(des)[2:ndigits+2])
    other = int(str(des)[ndigits+2:ndigits+3])
    res = 0
    if other >= 5:
        res = 1
    #print(des, ch1, other, res)
    return celoe + (ch1 + res) / 10 ** ndigits


print(my_round(2.1234567, 5))
print(my_round(2.1234545352, 8))
print(my_round(2.12, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

