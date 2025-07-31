from game_pole_class import pole

class BaseFigure:
    "Класс для описания примитивной фигуры. Базовый класс для всех фигур"

    def __init__(self, x, y, team=True): # функция для инициализации фигуры

        """
         x1, x2 - координаты начальной позиции фигуры (на шахматной доске).
         team - команда, за которую создаётся фигура (True - белые, False - чёрные)
        """
        if self._check_coords(x, y):
            if pole.pole[x][y]!='☐':
                raise Exception

            self._temp_x = None
            self._temp_y = None

            self._x = x
            self._y = y
            self._team = bool(team)
            pole(self)

    def _check_coords(self, x, y): # функция для проверки координат

        """
        Функция принимает координаты и проверяет их. Если координаты -
        не целые числа или не в диапазоне от 0 до 9, то генерируется исключение
        """

        if type(x)!=int or type(y)!=int:
            raise TypeError

        if 0 <= x <= 7 and 0 <= y <= 7:
            return True

        raise ValueError("Некорректные координаты")

    def __str__(self): # функция для вывода информации и фигуре
        if self._team:
            return f"Фигура: примитив\nРасположение: {(self._x, self._y)}\nКоманда: белые"
        return f"Фигура: примитив\nРасположение: {(self._x, self._y)}\nКоманда: чёрные\n"

    def __call__(self, x, y, *args, **kwargs): # ход фигуры
        """
        Магический метод для хода фигуры. Если на координаты x, y фигура
        может переместится, то координаты меняются. Иначи нет
        """
        if self._true_motion(x, y):
            self._temp_x = self._x
            self._temp_y = self._y

            self._x = x
            self._y = y
            pole(self)

    def _true_motion(self, x, y):
        pass