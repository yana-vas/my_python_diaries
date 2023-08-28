def look_around(r, c, matrix, rows):
    power = 0
    # Up left:
    if r - 2 in range(rows) and c - 1 in range(rows):
        if matrix[r - 2][c - 1] == 'K':
            power += 1
    # Up right:
    if r - 2 in range(rows) and c + 1 in range(rows):
        if matrix[r - 2][c + 1] == 'K':
            power += 1
    # Down left:
    if r + 2 in range(rows) and c - 1 in range(rows):
        if matrix[r + 2][c - 1] == 'K':
            power += 1
    # Down right:
    if r + 2 in range(rows) and c + 1 in range(rows):
        if matrix[r + 2][c + 1] == 'K':
            power += 1
    # Left up:
    if r - 1 in range(rows) and c - 2 in range(rows):
        if matrix[r - 1][c - 2] == 'K':
            power += 1
    # Left down:
    if r + 1 in range(rows) and c - 2 in range(rows):
        if matrix[r + 1][c - 2] == 'K':
            power += 1
    # Right up:
    if r - 1 in range(rows) and c + 2 in range(rows):
        if matrix[r - 1][c + 2] == 'K':
            power += 1
    # Right down:
    if r + 1 in range(rows) and c + 2 in range(rows):
        if matrix[r + 1][c + 2] == 'K':
            power += 1
    return power


def get_knights():
    strongest_coordinates = [0, 0, 0]
    for r in range(rows):
        for c in range(rows):
            if matrix[r][c] == 'K':
                power = look_around(r, c, matrix, rows)
                if power > 0 and power > strongest_coordinates[2]:
                    strongest_coordinates = [r, c, power]
    return strongest_coordinates


rows = int(input())
matrix = [list(input()) for _ in range(rows)]

strongest_info = get_knights()
count = 0

while not strongest_info[2] == 0:
    r, c = strongest_info[0], strongest_info[1]
    matrix[r][c] = '0'
    strongest_info = get_knights()
    count += 1

print(count)