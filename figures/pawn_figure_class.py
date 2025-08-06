from figures.base_figure_class import BaseFigure
from game_pole_class import pole
from motion_exception import *


class PawnFigure(BaseFigure):
    "Класс для описания пешки"

    def _true_motion(self, x, y):
        "Функция для проверки корректности хода пешки"

        if self._team:  # если команда пешки - белые

            "если пешка ходит на 1 или 2 клетки вперёд и эти клетки свободные"
            if self._x - x in (1, 2) and self._y - y == 0 and type(pole.pole[x][y]) == str and type(pole.pole[x + 1][y]) == str:
                return True

            elif self._x - x == 1 and abs(self._y - y) == 1 and type(pole.pole[x][y]) != str and pole.pole[x][y]._team == False:
                return True

            else:
                raise MotionException("Неверный ход пешки")

        else:  # если команда пешки - чёрные

            if x - self._x in (1, 2) and self._y - y == 0 and type(pole.pole[x][y]) == str and type(pole.pole[x - 1][y]) == str:
                return True

            elif x - self._x == 1 and abs(self._y - y) == 1 and type(pole.pole[x][y]) != str and pole.pole[x][y]._team == True:
                return True

            else:
                raise MotionException("Неверный ход пешки")

    def __str__(self):
        if self._team:
            return '♟'  # если команда пешки - белые
        return '♙'  # если команда пешки - чёрные