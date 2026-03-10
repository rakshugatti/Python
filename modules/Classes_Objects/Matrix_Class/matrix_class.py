class Matrix:

    # Initialize matrix with 2D list
    def __init__(self, data):
        self.data = data

    # Pretty print matrix
    def __str__(self):
        result = ""
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"
        return result

    # Matrix addition
    def __add__(self, other):

        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have same dimensions for addition")

        result = []

        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)

    # Matrix multiplication
    def __mul__(self, other):

        if len(self.data[0]) != len(other.data):
            raise ValueError("Invalid dimensions for multiplication")

        result = []

        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                sum_val = 0
                for k in range(len(other.data)):
                    sum_val += self.data[i][k] * other.data[k][j]
                row.append(sum_val)
            result.append(row)

        return Matrix(result)

    # Matrix comparison
    def __eq__(self, other):
        return self.data == other.data

    # Transpose method
    def transpose(self):

        result = []

        for i in range(len(self.data[0])):
            row = []
            for j in range(len(self.data)):
                row.append(self.data[j][i])
            result.append(row)

        return Matrix(result)


# -------- Demonstration --------

m1 = Matrix([[1,2,3],
             [4,5,6]])

m2 = Matrix([[7,8,9],
             [1,2,3]])

m3 = Matrix([[1,2],
             [3,4],
             [5,6]])

print("Matrix 1:")
print(m1)

print("Matrix 2:")
print(m2)

print("Matrix Addition:")
print(m1 + m2)

print("Matrix Multiplication:")
print(m1 * m3)

print("Transpose of Matrix 1:")
print(m1.transpose())

print("Matrix Comparison:")
print(m1 == m2)