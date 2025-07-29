"""
Специальный файл для проверки функциональности классов и т.д.
"""

from game_pole_class import pole
from rook_figure_class import RookFigure

pole.draw()
print()


for i in range(8):
    for j in range(8):
        RookFigure(i,j)


pole.draw()