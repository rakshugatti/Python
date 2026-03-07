# List Comprehension Examples

import math

# (a) Generate a list of squares of even numbers from 1 to 50
even_squares = [x**2 for x in range(1, 51) if x % 2 == 0]
print("Squares of even numbers (1-50):")
print(even_squares)


# (b) Flatten a 2D list into 1D
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [num for row in matrix for num in row]

print("\nFlattened List:")
print(flattened)


# (c) Matrix multiplication using list comprehension
def matrix_multiply(A, B):
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B)))
               for j in range(len(B[0]))]
               for i in range(len(A))]
    return result

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print("\nMatrix Multiplication Result:")
print(matrix_multiply(A, B))


# (d) Filter words longer than 5 characters from a sentence
sentence = "Python programming makes software development powerful and flexible"

long_words = [word for word in sentence.split() if len(word) > 5]

print("\nWords longer than 5 characters:")
print(long_words)


# (e) Generate all pairs (i, j) where i + j is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

pairs = [(i, j) for i in range(1, 10) for j in range(1, 10) if is_prime(i + j)]

print("\nPairs (i, j) where i + j is prime:")
print(pairs)