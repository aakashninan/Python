"""Program to Build a Shape Factory@AakashNinan IMCA Rollno:02"""
from math import pi

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "square":
            return Square(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)
        else:
            return None

s = input("Enter shape (circle/square/rectangle): ").lower()

if s == "circle":
    r = float(input("Enter radius: "))
    shape = ShapeFactory.create_shape("circle", r)
elif s == "square":
    a = float(input("Enter side: "))
    shape = ShapeFactory.create_shape("square", a)
elif s == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    shape = ShapeFactory.create_shape("rectangle", l, w)
else:
    shape = None

if shape:
    print("Area:", shape.area())
else:
    print("Invalid shape")
