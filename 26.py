""" Write a class Vehicle and a subclass Car that adds model and price. Create an object and display all details.@AakashNinan IMCA Rollno;02"""
class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, year, model, price):
        super().__init__(make, year)
        self.model = model
        self.price = price

    def display_details(self):
        print("--- Car Details ---")
        self.display_info()
        print(f"Model: {self.model}")
        print(f"Price: ${self.price:,.2f}")
        print("-------------------")

my_car = Car(make="Toyota", year=2023, model="Camry", price=25000.00)

my_car.display_details()
