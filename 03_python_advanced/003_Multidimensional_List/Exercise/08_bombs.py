rows = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]
coordinates = input().split()
for i in range(len(coordinates)):
    row, col = [int(x) for x in coordinates[i].split(',')]
    number = matrix[row][col]
    if matrix[row][col] > 0:
        if row-1 in range(rows):
            if col-1 in range(rows):
                if matrix[row-1][col-1] > 0:
                    matrix[row-1][col-1] -= number
            if col+1 in range(rows):
                if matrix[row-1][col+1] > 0:
                    matrix[row-1][col+1] -= number
            if matrix[row-1][col] > 0:
                matrix[row-1][col] -= number
        if row+1 in range(rows):
            if col-1 in range(rows):
                if matrix[row+1][col-1] > 0:
                    matrix[row+1][col-1] -= number
            if col+1 in range(rows):
                if matrix[row+1][col+1] > 0:
                    matrix[row+1][col+1] -= number
            if matrix[row+1][col] > 0:
                matrix[row+1][col] -= number
        if col-1 in range(rows):
            if matrix[row][col - 1] > 0:
                matrix[row][col - 1] -= number
        if col+1 in range(rows):
            if matrix[row][col + 1] > 0:
                matrix[row][col + 1] -= number
        matrix[row][col] = 0
alive_cells = []
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] > 0:
            alive_cells.append(matrix[row][col])
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    print(*row)
