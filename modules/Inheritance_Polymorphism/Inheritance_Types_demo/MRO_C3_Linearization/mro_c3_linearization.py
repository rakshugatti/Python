# Demonstrating Method Resolution Order (MRO)

class A:
    def show(self):
        print("Method from class A")


class B(A):
    def show(self):
        print("Method from class B")


class C(A):
    def show(self):
        print("Method from class C")


class D(B, C):
    pass


# Create object
obj = D()

# Call method
obj.show()

# Display MRO
print("\nMethod Resolution Order:")
print(D.mro())