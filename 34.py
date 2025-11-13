"""Program to Demonstrate Polymorphism with Animal, Dog, and Cat@AakashNinan IMCA Rollno:02"""
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]

for a in animals:
    print(a.speak())
