rows = int(input())
commands = input().split()
matrix = [input().split() for _ in range(rows)]
coals_counter = 0
all_coals = 0
coals_coordinates = []
miner_coordinates = [[row, col] for row in range(rows) for col in range(rows) if matrix[row][col] == 's']
has_output = False
for line in matrix:
    if 'c' in line:
        for char in line:
            if char == 'c':
                all_coals += 1
miner_row, miner_col = miner_coordinates[0][0], miner_coordinates[0][1]
for command in commands:
    if command == 'up':
        if miner_row-1 in range(rows):
            miner_coordinates = [[miner_row-1, miner_col]]
    elif command == 'down':
        if miner_row+1 in range(rows):
            miner_coordinates = [[miner_row+1, miner_col]]
    elif command == 'left':
        if miner_col-1 in range(rows):
            miner_coordinates = [[miner_row, miner_col-1]]
    elif command == 'right':
        if miner_col+1 in range(rows):
            miner_coordinates = [[miner_row, miner_col+1]]
    miner_row, miner_col = miner_coordinates[0][0], miner_coordinates[0][1]
    if matrix[miner_row][miner_col] == 'c':
        coals_counter += 1
        matrix[miner_row][miner_col] = '*'
        coals_coordinates = [miner_row, miner_col]
        if coals_counter == all_coals:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            has_output = True
            break
    if matrix[miner_row][miner_col] == 'e':
        print(f"Game over! ({miner_row}, {miner_col})")
        has_output = True
        break

if not has_output:
    print(f"{all_coals-coals_counter} pieces of coal left. ({miner_coordinates[0][0]}, {miner_coordinates[0][1]})")


