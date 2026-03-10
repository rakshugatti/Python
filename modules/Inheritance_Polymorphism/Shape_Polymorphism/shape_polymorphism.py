import math

# Base Class
class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


# Rectangle Class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Circle Class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# Triangle Class
class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# -------- Demonstration of Polymorphism --------

shapes = []

# Input for Rectangle
l = float(input("Enter rectangle length: "))
w = float(input("Enter rectangle width: "))
shapes.append(Rectangle(l, w))

# Input for Circle
r = float(input("Enter circle radius: "))
shapes.append(Circle(r))

# Input for Triangle
a = float(input("Enter triangle side1: "))
b = float(input("Enter triangle side2: "))
c = float(input("Enter triangle side3: "))
shapes.append(Triangle(a, b, c))

print("\n--- Areas and Perimeters ---")

for s in shapes:
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())
    print()