def is_valid_coordinates(row, col, total_rows):
    return row in range(0, total_rows) and col in range(0, total_rows)


def print_matrix(matrix):
    for r in matrix:
        print(*r)


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
command = input()
while command != 'END':
    command = command.split()
    rol = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if is_valid_coordinates(rol, col, rows):
        if command[0] == 'Add':
            matrix[rol][col] += value
        elif command[0] == 'Subtract':
            matrix[rol][col] -= value
    else:
        print("Invalid coordinates")

    command = input()

print_matrix(matrix)