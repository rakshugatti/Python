Explanation
(a) Squares of Even Numbers
[x**2 for x in range(1,51) if x % 2 == 0]

Filters even numbers

Calculates square of each

(b) Flatten 2D List
[num for row in matrix for num in row]

Iterates through rows

Extracts each element

(c) Matrix Multiplication

Uses nested list comprehensions to compute the multiplication of matrices.

(d) Filter Long Words
[word for word in sentence.split() if len(word) > 5]

Splits sentence into words

Keeps words longer than 5 characters

(e) Prime Sum Pairs
[(i,j) for i in range(1,10) for j in range(1,10) if is_prime(i+j)]

Generates all pairs

Keeps pairs where sum is prime