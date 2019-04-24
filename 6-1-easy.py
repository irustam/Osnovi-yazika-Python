__author__ = 'Искендеров Рустам Эльдарович'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    a = list()
    b = list()
    c = list()
    ab = float()
    bc = float()
    ca = float()
    __square = float()

    def __init__(self, coord):
        self.a = coord[0]
        self.b = coord[1]
        self.c = coord[2]

    def count_square(self):
        self.__square = abs((self.a[0] - self.c[0]) * (self.b[1] - self.c[1]) - (self.b[0] - self.c[0]) * (self.a[1] - self.c[1])) / 2
        return self.__square

    def count_high(self):
        h1 = 2 * self.__square / self.ab
        h2 = 2 * self.__square / self.bc
        h3 = 2 * self.__square / self.ca
        return f'Высота из точки C {h1}\nВысота из точки A {h2}\nВысота из точки B {h3}'

    def count_perimeter(self):
        self.ab = math.sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2)
        self.bc = math.sqrt((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2)
        self.ca = math.sqrt((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2)
        return self.ab + self.bc + self.ca

coord = [(1, 4),
          (5, 8),
          (9, -2),]

figure = Triangle(coord)
print('Площадь треугольника', figure.count_square())
print('Периметр треугольника', figure.count_perimeter())
print(figure.count_high())

