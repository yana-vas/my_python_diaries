import sys


def find_starting_point(matrix):
    for r in range(len(matrix)):
        row = matrix[r]
        for c in range(len(row)):
            char = matrix[r][c]
            if char == 'B':
                return [r, c]


def look_around(matrix):
    directions_eggs_info = {'up': [0, []], 'down': [0, []], 'left': [0, []], 'right': [0, []]}
    r, c = bunny_coordination[0], bunny_coordination[1]

    # Up
    for i in range(1, r + 1):
        char = matrix[r - i][c]
        if char == 'X':
            break
        else:
            directions_eggs_info['up'][0] += int(char)
            directions_eggs_info['up'][1].append([r - i, c])

    # Down
    for i in range(1, len(matrix) - r):
        char = matrix[r + i][c]
        if char == 'X':
            break
        else:
            directions_eggs_info['down'][0] += int(char)
            directions_eggs_info['down'][1].append([r + i, c])

    # Left
    for i in range(1, c + 1):
        char = matrix[r][c - i]
        if char == 'X':
            break
        else:
            directions_eggs_info['left'][0] += int(char)
            directions_eggs_info['left'][1].append([r, c - i])

    # Right
    for i in range(1, len(matrix) - c):
        char = matrix[r][c + i]
        if char == 'X':
            break
        else:
            directions_eggs_info['right'][0] += int(char)
            directions_eggs_info['right'][1].append([r, c + i])

    most_eggs_direction_info = [0, 0, 0]  # direction, coordinates, eggs
    eggs = -sys.maxsize
    for direction, values in directions_eggs_info.items():
        curr_eggs = int(values[0])
        if curr_eggs > eggs:
            eggs = curr_eggs
            most_eggs_direction_info[0] = direction
            most_eggs_direction_info[1] = values[1]
            most_eggs_direction_info[2] = values[0]
    return most_eggs_direction_info



rows = int(input())
matrix = [input().split() for _ in range(rows)]
bunny_coordination = find_starting_point(matrix)
eggs_direction_info = look_around(matrix)

print(eggs_direction_info[0])
for coord in eggs_direction_info[1]:
    print(coord)
print(eggs_direction_info[2])


