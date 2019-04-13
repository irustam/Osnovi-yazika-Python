__author__ = 'Искендеров Рустам Эльдарович'

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = list(map(int, str(ticket_number)))
    p1, p2 = 0, 0
    for key, item in enumerate(ticket_number):
        if key >= len(ticket_number) - 3:
            p2 += item
        else:
            p1 += item

    if p2 - p1 == 0:
        return 'Lucky ticket!'
    else:
        return 'Usual ticket'


print(lucky_ticket(123006))
print(lucky_ticket(66))
print(lucky_ticket(12321))
print(lucky_ticket(436751))