# задача с соседним файлом на импорт класса. вычислить площадь

from Area import Rectangle, Square, Circle

f1 = Rectangle(10, 5)
f2 = Square(6)
f3 = Circle(8)

figures = [f1, f2, f3]

for figure in figures:
    if isinstance(figure, Square):
        print("Квадрат", figure.getAreaSquare())
    elif isinstance(figure, Circle):
        print("Круг", figure.getAreaCircle())
    else:
        print("Прямоугольник", figure.getArea())
