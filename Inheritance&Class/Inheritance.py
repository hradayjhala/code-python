class Vehicle:
    def general_usage(self):
        print("General Usage : Transportation")

class Car(Vehicle):
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("Specific Usage : Commute to work, Vacation with Family")

class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm a motorcycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("Specific Usage : Road Trip, Racing")

c = Car()

print()

m = Motorcycle()

print(issubclass(Car, Vehicle))
