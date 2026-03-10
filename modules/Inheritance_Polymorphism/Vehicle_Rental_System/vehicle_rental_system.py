# Base Class
class Vehicle:

    def __init__(self, name, rate_per_day, fuel_type):
        self.name = name
        self.rate_per_day = rate_per_day
        self.fuel_type = fuel_type
        self.available = True

    def calculate_rent(self, days):
        return self.rate_per_day * days


# Derived Classes
class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


class Truck(Vehicle):
    pass


# Rental Shop Class
class RentalShop:

    def __init__(self):
        self.vehicles = []

    # Add vehicle
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    # Display vehicles
    def show_vehicles(self):
        print("\nVehicle List:")
        for i, v in enumerate(self.vehicles):
            status = "Available" if v.available else "Booked"
            print(i, "-", v.name, "| Fuel:", v.fuel_type,
                  "| Rate:", v.rate_per_day,
                  "| Status:", status)

    # Book vehicle
    def book_vehicle(self, index, days):

        if index >= len(self.vehicles):
            print("Invalid vehicle")
            return

        vehicle = self.vehicles[index]

        if vehicle.available:
            bill = vehicle.calculate_rent(days)
            vehicle.available = False

            print("Vehicle booked:", vehicle.name)
            print("Total Bill:", bill)
        else:
            print("Vehicle already booked")

    # Return vehicle
    def return_vehicle(self, index):

        if index >= len(self.vehicles):
            print("Invalid vehicle")
            return

        vehicle = self.vehicles[index]
        vehicle.available = True
        print("Vehicle returned:", vehicle.name)


# ----------------------
# Main Program
# ----------------------

shop = RentalShop()

n = int(input("Enter number of vehicles: "))

for i in range(n):

    print("\nVehicle", i + 1)

    vtype = input("Enter vehicle type (car/bike/truck): ").lower()
    name = input("Enter vehicle name: ")
    rate = int(input("Enter rate per day: "))
    fuel = input("Enter fuel type: ")

    if vtype == "car":
        shop.add_vehicle(Car(name, rate, fuel))

    elif vtype == "bike":
        shop.add_vehicle(Bike(name, rate, fuel))

    elif vtype == "truck":
        shop.add_vehicle(Truck(name, rate, fuel))

    else:
        print("Invalid vehicle type")


while True:

    print("\n1. Show Vehicles")
    print("2. Book Vehicle")
    print("3. Return Vehicle")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        shop.show_vehicles()

    elif choice == 2:
        index = int(input("Enter vehicle number: "))
        days = int(input("Enter number of days: "))
        shop.book_vehicle(index, days)

    elif choice == 3:
        index = int(input("Enter vehicle number to return: "))
        shop.return_vehicle(index)

    elif choice == 4:
        print("Thank you for using Rental System")
        break

    else:
        print("Invalid choice")