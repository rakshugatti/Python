class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # String representation (user friendly)
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    # Developer representation
    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    # Length (returns quantity)
    def __len__(self):
        return self.quantity

    # Equality comparison
    def __eq__(self, other):
        return self.price == other.price

    # Less than comparison
    def __lt__(self, other):
        return self.price < other.price

    # Addition of two products
    def __add__(self, other):
        return self.price + other.price

    # Indexing on product name
    def __getitem__(self, index):
        return self.name[index]


# -------- Main Program --------

products = []

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    p = Product(name, price, quantity)
    products.append(p)


print("\nProduct Details")
for p in products:
    print(p)   # calls __str__


print("\nDeveloper Representation")
for p in products:
    print(repr(p))   # calls __repr__


print("\nProduct Quantities")
for p in products:
    print(p.name, "quantity:", len(p))   # calls __len__


# Compare first two products if available
if len(products) >= 2:
    p1 = products[0]
    p2 = products[1]

    print("\nComparisons between first two products")

    print("Equal price?", p1 == p2)   # __eq__
    print("p1 cheaper than p2?", p1 < p2)   # __lt__
    print("Total price:", p1 + p2)   # __add__
    print("First letter of p1 name:", p1[0])   # __getitem__