"""Program to Implement Abstract Class Shape with Rectangle@AakashNinan IMCA Rollno:02"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

l = int(input("Enter length: "))
w = int(input("Enter width: "))
rect = Rectangle(l, w)
print("Area of rectangle:", rect.area())
