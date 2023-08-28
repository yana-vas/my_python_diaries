# Multidimensional list - Nested List - Лист в листа

def print_matrix(matrix):
    for r in matrix:
        print(*r)


def creating_matrix():
    rows = int(input())
    matrix = [input().split() for _ in range(rows)]
    return matrix

# Creating MD with Zeros
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(2):
        matrix[i].append(0)
# [[0, 0], [0, 0], [0, 0]]

# Comprehensions

# Creating a matrix with zeros
matrix = [[0 for j in range(2)] for i in range(3)]
# Creating a matrix with numbers
matrix = [[j for j in range(1, 4)] for i in range(3)]

# Flattening a matrix
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix for num in sublist]
# [1, 2, 3, 4, 5, 6]

# Accessing Elements
# print(matrix[row][column])

# 3-dimensional list
matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(matrix[0][1][1])  # 4

# Traversing elements using loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in range(len(matrix)):
    line = matrix[row]
    for column in range(len(line)):
        element = matrix[row][column]
        print(element, end=' ')

# Traversing elements using comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[print(el) for el in [j for j in matrix]]

# Printing matrx using loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in range(len(matrix)):
    line = matrix[row]
    for column in range(len(line)):
        element = matrix[row][column]
    print(*line)
# 1 2 3
# 4 5 6
# 7 8 9

# Changing values - increasing each value by 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] += 1
print(matrix)
# [[2, 3, 4], [5, 6, 7], [8, 9 ,10]]

# Changing values
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] += 1
print(matrix)
# [[2, 3, 4], [5, 6, 7], [8, 9 ,10]]


# Usage
# When dealing with graphics (pixels on the screen are in a grid formation)
# When working with tabular data
# Game development
# Other cases when you want each item of your list to be another list (Example: list of students, each of which has many tests)

# Other Nested Structures

# Set
set_of_numbers = [{1, 2, 3}, {4, 5, 6}]

# Tuple
tuples_collection = [('petter', 'merry'), (22, 19)]

# Dictionary
students_and_grades = {"petter": [4.50, 5.000, 4.95], "anna": [6.00, 5.65, 5.80]}

# Tuples as dictionary values
words_and_characters = {
    "bob": ("b", "o", "b"),
    "anna": ("a", "n", "n", "a")
}
