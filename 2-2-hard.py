__author__ = 'Искендеров Рустам Эльдарович'

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'

# Примеры некорректных дат
#date = '01.22.1001'
#date = '1.12.1001'
#date = '-2.10.3001'

months_days = {1:31,
                2:28,
                3:31,
                4:30,
                5:31,
                6:30,
                7:31,
                8:31,
                9:30,
                10:31,
                11:30,
                12:31,}
year_min = 1
year_max = 9999
check = False

while not check:
    user_date = str(input('Enter date in format dd.mm.yyyy: '))
    user_date = user_date.replace('/','.')
    user_date = user_date.replace('-','.')

    if user_date.count('.') == 2:
        dot1 = user_date.find('.')
        dot2 = user_date.find('.',dot1+1)

        try:
            day = int(user_date[:dot1])
        except:
            day = 0

        try:
            month = int(user_date[dot1+1:dot2])
        except:
            month = 0

        try:
            year = int(user_date[dot2+1:])
        except:
            year = -1


        if 0 < month <= 12:
            if 0 < day <= months_days[month]:
                if year_min <= year <= year_max:
                    check = True
                else:
                    print('You entered not valid year')
            else:
                print('You entered not valid day')
        else:
            print('You entered not valid month')
    else:
        print('You entered not valid date')

day = '0' + str(day)
month = '0' + str(month)
year = '000' + str(year)

format_date = f'{day[-2:]}.{month[-2:]}.{year[-4:]}'

print(format_date)