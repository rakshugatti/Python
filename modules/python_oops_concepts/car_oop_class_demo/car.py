# Car class definition
class Car:

    # Constructor to initialize car attributes
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand      # attribute: car brand
        self.model = model      # attribute: car model
        self.year = year        # attribute: manufacturing year
        self.speed = speed      # attribute: current speed

    # Method to increase speed
    def accelerate(self):
        self.speed += 10
        print(self.brand, "accelerated to", self.speed, "km/h")

    # Method to decrease speed
    def brake(self):
        self.speed -= 5
        print(self.brand, "slowed to", self.speed, "km/h")

    # Method to display car information
    def display_info(self):
        print("\nCar Information")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Speed:", self.speed)


# Taking input for three cars
print("Enter details for Car 1")
brand1 = input("Enter brand: ")
model1 = input("Enter model: ")
year1 = int(input("Enter year: "))

print("\nEnter details for Car 2")
brand2 = input("Enter brand: ")
model2 = input("Enter model: ")
year2 = int(input("Enter year: "))

print("\nEnter details for Car 3")
brand3 = input("Enter brand: ")
model3 = input("Enter model: ")
year3 = int(input("Enter year: "))


# Creating car objects
car1 = Car(brand1, model1, year1)
car2 = Car(brand2, model2, year2)
car3 = Car(brand3, model3, year3)


# Demonstrating method calls
car1.display_info()
car1.accelerate()
car1.brake()

car2.display_info()
car2.accelerate()

car3.display_info()
car3.accelerate()
car3.accelerate()