def targets(matrix):
    all_targets = 0
    for row in matrix:
        for char in row:
            if char == 'x':
                all_targets += 1
    return all_targets


def find_starting_point(matrix):
    for r in range(len(matrix)):
        row = matrix[r]
        for c in range(len(row)):
            char = matrix[r][c]
            if char == 'A':
                return [r, c]


matrix = [input().split() for _ in range(5)]
my_position = find_starting_point(matrix)
number_of_commands = int(input())
total_targets = targets(matrix)
shot_targets = []
collected_targets = 0
for _ in range(number_of_commands):
    command = input().split()
    direction = command[1]
    if command[0] == 'move':

        step = int(command[2])
        r, c = my_position[0], my_position[1]
        if direction == 'up':
            for i in range(1, step+1):
                if r - i in range(len(matrix)):
                    char = matrix[r - i][c]
                    if char == '.':
                        matrix[r][c] = '.'
                        alice_coordination = [r - i, c]
        elif direction == 'down':
            for i in range(1, step+1):
                if r + i in range(len(matrix)):
                    char = matrix[r + i][c]
                    if char == '.':
                        matrix[r][c] = '.'
                        alice_coordination = [r + i, c]
        elif direction == 'left':
            for i in range(1, step+1):
                if c-i in range(len(matrix)):
                    char = matrix[r][c-i]
                    if char == '.':
                        matrix[r][c] = '.'
                        alice_coordination = [r, c-i]
        elif direction == 'right':
            for i in range(1, step+1):
                if c+i in range(len(matrix)):
                    char = matrix[r][c+i]
                    if char == '.':
                        matrix[r][c] = '.'
                        alice_coordination = [r, c+i]

    elif command[0] == 'shoot':
        r, c = my_position[0], my_position[1]
        if direction == 'up':
            for i in range(1, r + 1):
                char = matrix[r - i][c]
                if char == 'x':
                    shot_targets.append([r - i, c])
                    collected_targets += 1
                    matrix[r - i][c] = '.'
                    break
        elif direction == 'down':
            for i in range(1, len(matrix) - r):
                char = matrix[r + i][c]
                if char == 'x':
                    shot_targets.append([r + i, c])
                    collected_targets += 1
                    matrix[r + i][c] = '.'
                    break
        elif direction == 'left':
            for i in range(1, c + 1):
                char = matrix[r][c-i]
                if char == 'x':
                    shot_targets.append([r, c-i])
                    collected_targets += 1
                    matrix[r][c-i] = '.'
                    break
        elif direction == 'right':
            for i in range(1, len(matrix) - c):
                char = matrix[r][c+i]
                if char == 'x':
                    shot_targets.append([r, c+1])
                    collected_targets += 1
                    matrix[r][c+i] = '.'
                    break
if total_targets == collected_targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets-collected_targets} targets left.")
for position in shot_targets:
    print(position)