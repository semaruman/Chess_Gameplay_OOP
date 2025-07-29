class GamePole:
    """Класс для описания фигур на поле
    и последующего отображения"""

    def __init__(self):
        "инициализация игрового поля"
        self.pole = [ ['☐' for i in range(8)] for j in range(8) ] # отображение фигур будет на этом поле

    def draw(self):
        "отображение игрового поля в консоль (банальный вывод на экран)"

        print("  0  1 2 3  4 5  6 7")
        for i in range( len(self.pole) ):
            print(i, end=' ')

            for j in range(len(self.pole[i])):
                print(self.pole[i][j], end=' ')

            print()


    def __call__(self,figure, *args, **kwargs): # figure - объект класса какой-либо фигуры

        self.pole[figure._x][figure._y] = figure

        if figure._temp_x != None and figure._temp_y != None:
            "если предыдущее положение не None, то его обнуляю"
            self.pole[figure._temp_x][figure._temp_y] = '☐'

pole = GamePole()