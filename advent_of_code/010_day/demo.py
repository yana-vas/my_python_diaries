def print_matrix(matrix):
    for r in matrix:
        print(*r)


input_data = open("input_data.txt").read().splitlines()
matrix = [list(line) for line in open('matrix.txt').read().splitlines()]
x = 1
my_list = [20, 60, 100, 140, 180, 220]
sprite_position = 0
signal_strength = []
cycle_counter = 0
j = 0
r = 0
for line in input_data:
    line = line.split()
    command = line[0]
    if command == 'noop':
        for i in range(1):
            if j == 40:
                r += 1
                j = 0

            if sprite_position <= j <= sprite_position+2:
                matrix[r][j] = '#'
            cycle_counter += 1
            j += 1
            if cycle_counter in my_list:
                signal_strength.append(cycle_counter * x)
    if command == 'addx':
        value = int(line[1])
        for i in range(2):
            cycle_counter += 1
            if j == 40:
                r += 1
                j = 0
            if sprite_position <= j <= sprite_position+2:
                matrix[r][j] = '#'
            j += 1
            if cycle_counter in my_list:
                signal_strength.append(cycle_counter * x)
        x += value
        sprite_position = x-1
print(sum(signal_strength))
print_matrix(matrix)

