grid = [list(line) for line in open('example_matrix.txt').read().splitlines()]
commands = open('example.txt').read().splitlines()

# grid = [list(line) for line in open('matrix.txt').read().splitlines()]
# commands = open('input_data.txt.txt').read().splitlines()

s_row = H_row = T_row = 4
s_cow = H_col = T_col = 0
points = 1
counter = 0
second_part_points = 1
for command in commands:
    direction, moves = command.split()

    if direction == "R":
        for i in range(int(moves)):
            if 0 <= H_col+1 < len(grid[H_row]):
                if grid[H_row][H_col+1] != '#':
                    if grid[H_row][H_col] != '#':
                        grid[H_row][H_col] = "."
                    grid[H_row][H_col+1] = "H"
                H_col += 1
                if H_col-T_col > 1:
                    T_col += 1
                    grid[T_row][T_col - 1] = '#'
                    if T_row != H_row or T_col != H_col:
                        T_row = H_row
                    grid[H_row][H_col-1] = "T"

    elif direction == "L":
        for i in range(int(moves)):
            if 0 <= H_col - 1 < len(grid[H_row]):
                if grid[H_row][H_col-1] != '#':
                    if grid[H_row][H_col] != '#':
                        grid[H_row][H_col] = "."
                    grid[H_row][H_col-1] = "H"
                H_col -= 1
                if T_col - H_col > 1:
                    T_col -= 1
                    grid[T_row][T_col + 1] = '#'
                    if T_row != H_row or T_col != H_col:
                        T_row = H_row
                    grid[H_row][H_col + 1] = "T"
    elif direction == "U":
        for i in range(int(moves)):
            if 0 <= H_row-1 < len(grid):
                if grid[H_row-1][H_col] != '#':
                    if grid[H_row][H_col] != '#':
                        grid[H_row][H_col] = "."
                    grid[H_row-1][H_col] = "H"
                H_row -= 1
                if T_row-H_row > 1:
                    grid[T_row][T_col] = '#'
                    T_row -= 1
                    T_col = H_col
                    grid[T_row][T_col] = "T"

    elif direction == "D":
        for i in range(int(moves)):
            if 0 <= H_row+1 < len(grid):
                if grid[H_row+1][H_col] != '#':
                    if grid[H_row][H_col] != '#':
                        grid[H_row][H_col] = "."
                    grid[H_row+1][H_col] = "H"
                H_row += 1
                if H_row-T_row > 1:
                    grid[T_row][T_col] = '#'
                    T_row += 1
                    T_col = H_col
                    grid[T_row][T_col] = "T"


for line in grid:
    points += line.count('#')
print(points)










# https://pastebin.com/p57KNgHg