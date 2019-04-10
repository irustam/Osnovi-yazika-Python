__author__ = 'Искендеров Рустам Эльдарович'

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

months_name = {1:'января',
                2:'февраля',
                3:'марта',
                4:'апреля',
                5:'мая',
                6:'июня',
                7:'июля',
                8:'августа',
                9:'сентября',
                10:'октября',
                11:'ноября',
                12:'декабря',}
days_name = {1:'первое',
            2:'второе',
            3:'третье',
            4:'четвертое',
            5:'пятое',
            6:'шестое',
            7:'седьмое',
            8:'восьмое',
            9:'девятое',
            10:'десятое',
            11:'одинадцатое',
            12:'двенадцатое',
            13:'тринадцатое',
            14:'четырнадцатое',
            15:'пятнадцатое',
            16:'шестнадцатое',
            17:'семьнадцатое',
            18:'восемьнадцатое',
            19:'девятнадцатое',
            20:'двадцатое',
            21:'двадцать первое',
            22:'двадцать второе',
            23:'двадцать третье',
            24:'двадцать четвертое',
            25:'двадцать пятое',
            26:'двадцать шестое',
            27:'двадцать седьмое',
            28:'двадцать восьмое',
            29:'двадцать девятое',
            30:'тридцатое',
            31:'тридцать первое',}

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
            day = days_name[day]
            check = True
        except:
            check = False

        try:
            month = int(user_date[dot1+1:dot2])
            month = months_name[month]
            check = True
        except:
            check = False

        try:
            year = int(user_date[dot2+1:])
            check = True
        except:
            check = False
    else:
        print('You entered not valid date')

new_date = f'{day} {month} {year} года'
print(new_date)