__author__ = 'Искендеров Рустам Эльдарович'

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

max_rooms = 2000000000

# Получаем номер комнаты
check = False

while not check:
    room_number = input(f'Enter room number from 1 to {max_rooms}: ')
    try:
        room_number = int(room_number)
        check = True
        if not 0 < room_number <= max_rooms:
            check = False
    except:
        print('You entered not valid number')
################# Получили

# Запускаем лифт
first_room_on_floor = 1
first_floor = 1
square_size = 1
y = 1

while room_number > y:
    first_room_on_floor = y + 1
    first_floor = first_floor + square_size

    square_size += 1
    y = y + square_size ** 2
################# Лифт доехал до нужной матрицы

# Вычисляем этаж и позицию
room_id_in_square = room_number - first_room_on_floor + 1
room_position = room_id_in_square % square_size

if room_position == 0:
    room_position = square_size
    room_floor = int(room_id_in_square / square_size + first_floor - 1)
else:
    room_floor = int(room_id_in_square // square_size + first_floor)

################# Вычислили этаж и позицию на этаже

#print(f'Room {first_room_on_floor} | Floor {first_floor} | Square {square_size} | Room ID in square {room_id_in_square}')
print(f'Room floor {room_floor} | Room position {room_position}')

