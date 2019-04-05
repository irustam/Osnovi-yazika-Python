__author__ = 'Искендеров Рустам Эльдарович'

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = input('Enter your age: ')
check = False

while check == False:
    try:
        age = int(age)
        check = True
    except:
        age = input('You entered not age. Enter your age: ')

if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')