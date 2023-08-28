rows, columns = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = list(input())
player_coordinates = []
for row in range(rows):
    for col in range(columns):
        if matrix[row][col] == 'P':
            player_coordinates.append([row, col])

state = None

p_row, p_col = player_coordinates[0][0], player_coordinates[0][1]
for command in commands:
    bunnies_coordinates = []

    if command == 'U':
        if p_row - 1 in range(rows) and state is None:
            if matrix[p_row-1][p_col] == 'B':
                state = 'dead'
            matrix[p_row][p_col] = '.'
            player_coordinates = [[p_row - 1, p_col]]
            p_row, p_col = player_coordinates[0][0], player_coordinates[0][1]
        else:
            state = 'won'
            matrix[p_row][p_col] = '.'
    elif command == 'D':
        if p_row + 1 in range(rows) and state is None:
            if matrix[p_row+1][p_col] == 'B':
                state = 'dead'
            matrix[p_row][p_col] = '.'
            player_coordinates = [[p_row + 1, p_col]]
            p_row, p_col = player_coordinates[0][0], player_coordinates[0][1]
        else:
            state = 'won'
            matrix[p_row][p_col] = '.'
    elif command == 'L':
        if p_col - 1 in range(rows) and state is None:
            if matrix[p_row][p_col-1] == 'B':
                state = 'dead'
            matrix[p_row][p_col] = '.'
            player_coordinates = [[p_row, p_col-1]]
            p_row, p_col = player_coordinates[0][0], player_coordinates[0][1]

        else:
            state = 'won'
            matrix[p_row][p_col] = '.'
    elif command == 'R':
        if p_col + 1 in range(rows) and state is None:
            if matrix[p_row][p_col+1] == 'B':
                state = 'dead'
            matrix[p_row][p_col] = '.'
            player_coordinates = [[p_row, p_col + 1]]
            p_row, p_col = player_coordinates[0][0], player_coordinates[0][1]
        else:
            state = 'won'
            matrix[p_row][p_col] = '.'

    for row in range(rows):
        for col in range(columns):
            char = matrix[row][col]
            if char == 'B':
                bunnies_coordinates.append([row, col])
    for indexes in bunnies_coordinates:
        row, col = indexes[0], indexes[1]
        if row - 1 in range(rows):
            matrix[row - 1][col] = 'B'
        if row + 1 in range(rows):
            matrix[row + 1][col] = 'B'
        if col - 1 in range(columns):
            matrix[row][col - 1] = 'B'
        if col + 1 in range(columns):
            matrix[row][col + 1] = 'B'
    if state is not None:
        if state == 'dead':
            p_row, p_col = player_coordinates[0][0], player_coordinates[0][1]
        else:
            matrix[p_row][p_col] = '.'
        break
    p_row, p_col = player_coordinates[0][0], player_coordinates[0][1]

for line in matrix:
    print(*line, sep='')

if state == 'won':
    print(f"won: {p_row} {p_col}")
else:
    print(f"dead: {p_row} {p_col}")

