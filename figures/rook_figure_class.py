from figures.base_figure_class import BaseFigure
from game_pole_class import pole
from motion_exception import *

class RookFigure(BaseFigure):
    "Класс для описания ладьи"

    def _true_motion(self, x, y):
        "Функция для проверки корректности хода ладьи"

        if self._x - x == 0 or self._y - y==0:
            """Если ладья ходит прямо, то ничего делать не надо.
            Иначе генерируется ошибка о неправильном ходе"""
        else:
            raise WrongFigureMotion("Ладья не может так ходить")

        if type(pole.pole[x][y])==str:
            return True

        if pole.pole[x][y]._team == self._team:
            "Если ладья ходит на место своей фигуры, то генерируется ошибка"
            raise EatYourFigureException("Нельзя ходить на место своей фигуры")

        "Любой другой ход будет правильным, поэтому функция вернёт True"
        return True

    def __str__(self):
        if self._team:
            return '♜' # если команда ладьи - белые
        return '♖' # если команда ладьи - чёрные