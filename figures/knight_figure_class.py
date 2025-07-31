from figures.base_figure_class import BaseFigure
from game_pole_class import pole
from motion_exception import *

class KnightFigure(BaseFigure):
    "Класс для описания коня"

    def _true_motion(self, x, y):
        "Функция для проверки корректности хода коня"

        if abs(self._x - x) == 1 and abs(self._y - y)==2 or abs(self._x - x) == 2 and abs(self._y - y)==1:
            """Если конь ходит буквой Г, то ничего делать не надо.
            Иначе генерируется ошибка о неправильном ходе"""
        else:
            raise WrongFigureMotion("Конь не может так ходить")

        if type(pole.pole[x][y])==str:
            return True

        if pole.pole[x][y]._team == self._team:
            "Если конь ходит на место своей фигуры, то генерируется ошибка"
            raise EatYourFigureException("Нельзя ходить на место своей фигуры")

        "Любой другой ход будет правильным, поэтому функция вернёт True"
        return True

    def __str__(self):
        if self._team:
            return '♞' # если команда - белые
        return '♘' # если команда - чёрные