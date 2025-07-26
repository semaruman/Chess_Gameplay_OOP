"""
Специальный файл для проверки функциональности классов и т.д.
"""

from base_figure_class import BaseFigure


bf = BaseFigure(0,0) # создал примитивную фигуру
print(bf)
print()

bf(1,2) # сделал ход
print(bf)
print()

print(BaseFigure.__doc__) # вывел информацию о базовом классе