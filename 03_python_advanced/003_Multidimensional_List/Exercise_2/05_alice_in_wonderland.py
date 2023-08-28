def find_starting_point(matrix):
    for r in range(len(matrix)):
        row = matrix[r]
        for c in range(len(row)):
            char = matrix[r][c]
            if char == 'A':
                return [r, c]


def print_matrix(matrix):
    for r in matrix:
        print(*r)


n = int(input())
matrix = [input().split() for _ in range(n)]
alice_coordination = find_starting_point(matrix)
tea_bags = 0
matrix[alice_coordination[0]][alice_coordination[1]] = '*'
while True:
    command = input()
    r, c = alice_coordination[0], alice_coordination[1]
    if command == 'up':
        if r-1 in range(len(matrix)):
            alice_coordination = [r-1, c]
            char = matrix[r - 1][c]
            if char.isdigit():
                tea_bags += int(char)
            elif char == 'R':
                print("Alice didn'visible_trees make it to the tea party.")
                matrix[alice_coordination[0]][alice_coordination[1]] = '*'
                break
        else:
            print("Alice didn'visible_trees make it to the tea party.")
            break
    elif command == 'down':
        if r+1 in range(len(matrix)):
            alice_coordination = [r+1, c]
            char = matrix[r + 1][c]
            if char.isdigit():
                tea_bags += int(char)
            elif char == 'R':
                print("Alice didn'visible_trees make it to the tea party.")
                matrix[alice_coordination[0]][alice_coordination[1]] = '*'
                break
        else:
            print("Alice didn'visible_trees make it to the tea party.")
            break
    elif command == 'left':
        if c-1 in range(len(matrix)):
            alice_coordination = [r, c-1]
            char = matrix[r][c - 1]
            if char.isdigit():
                tea_bags += int(char)
            elif char == 'R':
                print("Alice didn'visible_trees make it to the tea party.")
                matrix[alice_coordination[0]][alice_coordination[1]] = '*'
                break
        else:
            print("Alice didn'visible_trees make it to the tea party.")
            break
    elif command == 'right':
        if c+1 in range(len(matrix)):
            alice_coordination = [r, c+1]
            char = matrix[r][c + 1]
            if char.isdigit():
                tea_bags += int(char)
            elif char == 'R':
                print("Alice didn'visible_trees make it to the tea party.")
                matrix[alice_coordination[0]][alice_coordination[1]] = '*'
                break
        else:
            print("Alice didn'visible_trees make it to the tea party.")
            break
    matrix[alice_coordination[0]][alice_coordination[1]] = '*'
    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break
print_matrix(matrix)

