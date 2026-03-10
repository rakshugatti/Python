# Hierarchical Inheritance
#Vehicle->Car,Vehicle->Bike
class Vehicle:

    def start(self):
        print("Vehicle starts")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


class Bike(Vehicle):

    def ride(self):
        print("Bike is riding")


c = Car()
b = Bike()

c.start()
c.drive()

b.start()
b.ride()