__author__ = 'Искендеров Рустам Эльдарович'

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math

class Triangle:
    a = list()
    b = list()
    c = list()
    d = list()
    ab = float()
    bc = float()
    cd = float()
    da = float()
    __square = float()

    def __init__(self, coord):
        self.a = coord[0]
        self.b = coord[1]
        self.c = coord[2]
        self.d = coord[3]

    def count_square(self):
        tr1 = abs((self.a[0] - self.c[0]) * (self.b[1] - self.c[1]) - (self.b[0] - self.c[0]) * (self.a[1] - self.c[1])) / 2
        tr2 = abs((self.a[0] - self.d[0]) * (self.c[1] - self.d[1]) - (self.c[0] - self.d[0]) * (self.a[1] - self.d[1])) / 2
        self.__square = tr1 + tr2
        return self.__square

    def check_equals(self):
        if self.ab == self.cd or self.bc == self.da:
            return 'Это равнобедренная трапеция'
        else:
            return 'Это не равнобедренная трапеция'


    def count_sides(self):
        self.ab = math.sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2)
        self.bc = math.sqrt((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2)
        self.cd = math.sqrt((self.c[0] - self.d[0]) ** 2 + (self.c[1] - self.d[1]) ** 2)
        self.da = math.sqrt((self.d[0] - self.a[0]) ** 2 + (self.d[1] - self.a[1]) ** 2)
        return f'Длина AB {self.ab}\nДлина BC {self.bc}\nДлина CD {self.cd}\nДлина AD {self.da}'

    def count_perimeter(self):
        return self.ab + self.bc + self.cd + self.da

coord = [(1, 4),
         (2, 8),
         (10, 8),
         (11, 4),]

figure = Triangle(coord)
print('Площадь четырехугольника', figure.count_square())
print(figure.count_sides())
print('Периметр четырехугольника', figure.count_perimeter())
print(figure.check_equals())

