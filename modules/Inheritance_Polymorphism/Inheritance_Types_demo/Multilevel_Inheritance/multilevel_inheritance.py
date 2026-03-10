# Multilevel Inheritance
# Animal->Mammal->Dog

class Animal:

    def eat(self):
        print("Animal eats food")


class Mammal(Animal):

    def walk(self):
        print("Mammal walks")


class Dog(Mammal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.walk()
d.bark()