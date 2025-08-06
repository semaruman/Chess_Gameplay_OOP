from game_pole_class import pole
from figures.king_figure_class import KingFigure


def black_win():
    """
    функция работает следующим образом:
    идёт перебор всего игрового поля. Если на поле
    не оказывается белого короля, то чёрные выигрывают

    """
    result = True

    for i in pole.pole:
        for j in i:
            if isinstance(j, KingFigure) and j._team == True:
                result = False

    return result