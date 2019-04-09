__author__ = 'Искендеров Рустам Эльдарович'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

equation = equation.replace(' ','')

where_k = equation.find('=')+1
where_x = equation.find('x')

k = float(equation[where_k:where_x])
b = equation[where_x+1:]
b = float(b.replace('+',''))

y = k * x + b

print(y)

