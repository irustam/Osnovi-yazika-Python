__author__ = 'Искендеров Рустам Эльдарович'

#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random

class Bag:
    get_keg = property()
    def __init__(self):
        self.kegs = [i for i in range(1, 91)]


    @get_keg.getter
    def get_keg(self):
        if len(self.kegs) > 0:
            take_keg = random.choice(self.kegs)
            self.kegs.remove(take_keg)
        else: take_keg = None
        return take_keg

class Ticket:
    def __init__(self, name):
        self.name = name
        nums = random.sample(range(1, 91), 16)
        self.line1 = sorted(nums[:5])
        self.line2 = sorted(nums[5:10])
        self.line3 = sorted(nums[11:16])
        for _ in range(0, 4):
            self.line1.insert(random.randint(0,len(self.line1)),' ')
            self.line2.insert(random.randint(0,len(self.line2)),' ')
            self.line3.insert(random.randint(0,len(self.line3)),' ')

    def __str__(self):
        if len(self.name) - 2 < 26:
            i = (26 - len(self.name) - 2) // 2
            n = 26 - len(self.name) - 2 - i
        else:
            i, n = 0, 0
        a = '-' * i + ' ' + self.name + ' ' + '-' * n + '\n' + \
        '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*self.line1) + '\n' + \
        '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*self.line2) + '\n' + \
        '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*self.line3) + '\n' + '-' * 26
        #a = self.name + '\n' + str(self.line1) + '\n' + str(self.line2) + '\n' + str(self.line3) + '\n' + str('-' * 26)
        return a

    def check_keg(self, keg):
        if keg in self.line1:
            for key, itm in enumerate(self.line1):
                if itm == keg:
                    self.line1[key] = '-'
                    win = self.__check_win()
                    return win or True
        elif keg in self.line2:
            for key, itm in enumerate(self.line2):
                if itm == keg:
                    self.line2[key] = '-'
                    win = self.__check_win()
                    return win or True
        elif keg in self.line3:
            for key, itm in enumerate(self.line3):
                if itm == keg:
                    self.line3[key] = '-'
                    win = self.__check_win()
                    return win or True
        else:
            return False

    def __check_win(self):
        all_lines = self.line1 + self.line2 + self.line3
        if all_lines.count('-') == 15:
            return 'Победа!'
        else:
            return False

class Game:
    __whatnext = property()

    def __init__(self):
        self.player = input('Как Вас зовут?')
        self.gamebag = Bag()
        self.player_ticket = Ticket(f'Билет игрока {self.player}')
        self.comp_ticket = Ticket('Билет компьютера')
        self.__current_result()

    def start(self):
        keg = self.gamebag.get_keg
        if keg:
            print(f'Новый бочонок из мешка: {keg}. Осталось: {len(self.gamebag.kegs)} бочонков в мешке', )

            res = self.__check_results(self.player_ticket.check_keg(keg), self.comp_ticket.check_keg(keg), self.__whatnext)
            if res:
                print(res)
            else:
                self.__current_result()
                self.start()
        else:
            print('Бочонки в мешке закончились')

    def __current_result(self):
        print(self.player_ticket)
        print(self.comp_ticket)

    @__whatnext.getter
    def __whatnext(self):
        try:
            whatnext = input('Зачеркнуть цифру? (y/n)')
        except KeyboardInterrupt:
            whatnext = 'exit'
        except TimeoutError:
            whatnext = 'exit'
        return whatnext

    def __check_results(self, player_res, comp_res, whatnext):
        if whatnext == 'y':
            if not player_res:
                return 'Game over'
            elif player_res == 'Победа!':
                if comp_res == 'Победа!':
                    return 'Ничья'
                else:
                    return 'Победа!'
            else:
                if comp_res == 'Победа!':
                    return 'Компьютер победил'
                else:
                    return False
        elif whatnext == 'n':
            if not player_res:
                if comp_res == 'Победа!':
                    return 'Компьютер победил'
                else:
                    return False
            else:
                return 'Game over'
        else:
            return 'Вы вышли из игры!'


mygame = Game()
mygame.start()

