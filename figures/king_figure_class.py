from figures.base_figure_class import BaseFigure
from game_pole_class import pole
from motion_exception import *

class KingFigure(BaseFigure):
    "Класс для описания Короля"

    def _true_motion(self, x, y):
        "Функция для проверки корректности хода короля"

        if abs(self._x - x) in (0, 1) and abs(self._y - y) in (0, 1):
            """Если король перемещается на 1 клетку, то ничего делать не надо.
            Иначе генерируется ошибка о неправильном ходе"""
        else:
            raise WrongFigureMotion("Король не может так ходить")

        if type(pole.pole[x][y])==str:
            return True

        if pole.pole[x][y]._team == self._team:
            "Если король ходит на место своей фигуры, то генерируется ошибка"
            raise EatYourFigureException("Нельзя ходить на место своей фигуры")

        "Любой другой ход будет правильным, поэтому функция вернёт True"
        return True

    def __str__(self):
        if self._team:
            return '♚' # если команда короля - белые
        return '♔' # если команда короля - чёрные