rows, cols = [int(x) for x in input().split(' ')]
matrix = [input().split(' ') for _ in range(rows)]

command = input()
while command != 'END':
    command = command.split()
    if command[0] == "swap" and len(command) == 5:
        if int(command[1]) in range(rows) \
                and int(command[2]) in range(cols) \
                and int(command[3]) in range(rows) \
                and int(command[4]) in range(cols) \
                and int(command[1]) >= 0 \
                and int(command[2]) >= 0 \
                and int(command[3]) >= 0 \
                and int(command[4]) >= 0:
            matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
            for line in matrix:
                print(*line)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()
