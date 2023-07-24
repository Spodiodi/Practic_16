import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

class Square:
    def __init__(self, a):
        self.a = a

    def getAreaSquare(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

    def getAreaCircle(self):
        return int(self.r ** 2 * math.pi)