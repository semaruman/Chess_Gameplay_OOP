class BaseFigure:

    def _check_coords(self, x, y): # функция для проверки координат

        """
        Функция принимает координаты и проверяет их. Если координаты -
        не целые числа или не в диапазоне от 0 до 9, то генерируется исключение
        """

        if type(x)!=int or type(y)!=int:
            raise TypeError

        if 0 <= x <=9 and 0 <= y <=9:
            return True

        raise ValueError("Некорректные координаты")


    def __init__(self, x, y, team=True): # функция для инициализации фигуры

        """
         x1, x2 - координаты начальной позиции фигуры (на шахматной доске).
         team - команда, за которую создаётся фигура (True - белые, False - чёрные)
        """
        if self._check_coords(x, y):
            self._x = x
            self._y = y
            self._team = bool(team)


    def __str__(self): # функция для вывода информации и фигуре
        if self._team:
            return f"Фигура: примитив\nРасположение: {(self._x, self._y)}\nКоманда: белые"
        return f"Фигура: примитив\nРасположение: {(self._x, self._y)}\nКоманда: чёрные\n"


    def __call__(self, x, y, *args, **kwargs): # ход фигуры
        """
        Магический метод для хода фигуры. Если на координаты x, y фигура
        может переместится, то координаты меняются. Иначи нет
        """
        if self._true_motion:
            self._x = x
            self._y = y


    def _true_motion(self, x, y):
        pass