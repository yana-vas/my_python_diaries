def print_matrix(matrix):
    for r in matrix:
        print(*r)


rows = columns = int(input())

matrix = [input().split(' ') for _ in range(rows)]
matrix = matrix[::-1]
rotated_matrix = []
for j in range(len(matrix)):
    row = matrix[j]
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    rotated_matrix.append(new_row)

print_matrix(rotated_matrix)
