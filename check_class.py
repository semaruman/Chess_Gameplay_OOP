"""
Специальный файл для проверки функциональности классов и т.д.
"""

pole.draw()
print()

bh = BishopFigure(0,0,False)
pole.draw()

bh(5,5)

r = RookFigure(1,5)
pole.draw()

r(5,5)
r(1,5)
pole.draw()
