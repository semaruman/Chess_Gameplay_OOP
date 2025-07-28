class MotionException(Exception):
    """Исключение, которое будет вызываться,
    когда пользователь будет ходить неверно"""


class WrongFigureMotion(MotionException):
    """Исключение, которое будет вызываться,
    когда фигура ходит неверно"""


class EatYourFigure(WrongFigureMotion):
    """Исключение, которое будет вызываться,
    когда фигура пытается сходить на место своей фигуры"""