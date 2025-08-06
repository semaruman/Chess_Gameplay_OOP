from game_pole_class import pole
from figures.king_figure_class import KingFigure

def white_win():
    """
    функция работает следующим образом:
    идёт перебор всего игрового поля. Если на поле
    не оказывается чёрного короля, то белые выигрывают

    """
    result = True

    for i in pole.pole:
        for j in i:
            if isinstance(j, KingFigure) and j._team == False:
                result = False

    return result