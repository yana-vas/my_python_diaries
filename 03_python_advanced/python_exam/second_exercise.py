def find_position(m):
    for r_index in range(len(m)):
        row = m[r_index]
        for c_index in range(len(row)):
            char = m[r_index][c_index]
            if char == 'T':
                return [r_index, c_index]


def print_matrix(matrix):
    for r in matrix:
        print(*r, sep='')


rows = int(input())  # rows in square matrix
racing_number = input()
matrix = [input().split() for _ in range(rows)]
race_car_coord = [0, 0]
km = 0

while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break
    elif command == 'up':
        race_car_coord[0] -= 1
        r, c = race_car_coord[0], race_car_coord[1]
        if matrix[r][c] == '.':
            km += 10
        elif matrix[r][c] == 'T':
            matrix[r][c] = '.'
            race_car_coord = find_position(matrix)
            matrix[race_car_coord[0]][race_car_coord[1]] = '.'
            km += 30
        elif matrix[r][c] == 'F':
            km += 10
            print(f"Racing car {racing_number} finished the stage!")
            break
    elif command == 'down':
        race_car_coord[0] += 1
        r, c = race_car_coord[0], race_car_coord[1]
        if matrix[r][c] == '.':
            km += 10
        elif matrix[r][c] == 'T':
            matrix[r][c] = '.'
            race_car_coord = find_position(matrix)
            matrix[race_car_coord[0]][race_car_coord[1]] = '.'
            km += 30
        elif matrix[r][c] == 'F':
            km += 10
            print(f"Racing car {racing_number} finished the stage!")
            break
    elif command == 'right':
        race_car_coord[1] += 1
        r, c = race_car_coord[0], race_car_coord[1]
        if matrix[r][c] == '.':
            km += 10
        elif matrix[r][c] == 'T':
            matrix[r][c] = '.'
            race_car_coord = find_position(matrix)
            matrix[race_car_coord[0]][race_car_coord[1]] = '.'
            km += 30
        elif matrix[r][c] == 'F':
            km += 10
            print(f"Racing car {racing_number} finished the stage!")
            break
    elif command == 'left':
        race_car_coord[1] -= 1
        r, c = race_car_coord[0], race_car_coord[1]
        if matrix[r][c] == '.':
            km += 10
        elif matrix[r][c] == 'T':
            matrix[r][c] = '.'
            race_car_coord = find_position(matrix)
            matrix[race_car_coord[0]][race_car_coord[1]] = '.'
            km += 30
        elif matrix[r][c] == 'F':
            km += 10
            print(f"Racing car {racing_number} finished the stage!")
            break

print(f"Distance covered {km} km.")
matrix[race_car_coord[0]][race_car_coord[1]] = 'C'
print_matrix(matrix)


