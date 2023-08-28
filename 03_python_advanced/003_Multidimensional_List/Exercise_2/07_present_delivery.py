def find_santa_position(matrix):
    for r in range(len(matrix)):
        row = matrix[r]
        for c in range(len(row)):
            char = matrix[r][c]
            if char == 'S':
                return [r, c]


number_of_presents = int(input())
n = int(input())  # rows
matrix = [input().split() for _ in range(n)]


def nice_kids_count(matrix):
    kids = 0
    for r in range(len(matrix)):
        row = matrix[r]
        for c in range(len(row)):
            char = matrix[r][c]
            if char == 'V':
                kids += 1
    return kids


def print_matrix(matrix):
    for r in matrix:
        print(*r)


all_nice_kids = nice_kids_count(matrix)
count_nice_kids = 0
santa_position = find_santa_position(matrix)
command = input()

while command != 'Christmas morning':
    r, c = santa_position[0], santa_position[1]
    if command == 'up':
        if r - 1 in range(len(matrix)):
            char = matrix[r - 1][c]
            if char == 'V':
                santa_position = [r - 1, c]
                count_nice_kids += 1
                number_of_presents -= 1
            elif char == 'X':
                santa_position = [r - 1, c]
            elif char == 'C':
                r, c = santa_position[0], santa_position[1]
                matrix[r][c] = '-'
                santa = [r - 1, c]
                r, c = santa[0], santa[1]

                if r - 1 in range(len(matrix)):
                    ch = matrix[r - 1][c]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r - 1][c] = '-'
                if r + 1 in range(len(matrix)):
                    ch = matrix[r + 1][c]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r + 1][c] = '-'
                if c - 1 in range(len(matrix)):
                    ch = matrix[r][c - 1]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r][c - 1] = '-'
                if c + 1 in range(len(matrix)):
                    ch = matrix[r][c + 1]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r][c + 1] = '-'

            matrix[r][c] = '-'
        matrix[r-1][c] = 'S'
        santa_position = [r-1, c]
    elif command == 'down':
        if r + 1 in range(len(matrix)):
            char = matrix[r + 1][c]
            if char == 'V':
                count_nice_kids += 1
                number_of_presents -= 1
            elif char == 'X':
                pass
            elif char == 'C':
                r, c = santa_position[0], santa_position[1]
                matrix[r][c] = '-'
                santa = [r - 1, c]
                r, c = santa[0], santa[1]

                if r - 1 in range(len(matrix)):
                    ch = matrix[r - 1][c]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r - 1][c] = '-'
                if r + 1 in range(len(matrix)):
                    ch = matrix[r + 1][c]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r + 1][c] = '-'
                if c - 1 in range(len(matrix)):
                    ch = matrix[r][c - 1]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r][c - 1] = '-'
                if c + 1 in range(len(matrix)):
                    ch = matrix[r][c + 1]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r][c + 1] = '-'
            matrix[r][c] = '-'
            matrix[r+1][c] = 'S'
            santa_position = [r+1, c]
    elif command == 'left':
        if c - 1 in range(len(matrix)):
            char = matrix[r][c-1]
            if char == 'V':
                count_nice_kids += 1
                number_of_presents -= 1
            elif char == 'X':
                pass
            elif char == 'C':
                r, c = santa_position[0], santa_position[1]
                matrix[r][c] = '-'
                santa = [r - 1, c]
                r, c = santa[0], santa[1]

                if r - 1 in range(len(matrix)):
                    ch = matrix[r - 1][c]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r - 1][c] = '-'
                if r + 1 in range(len(matrix)):
                    ch = matrix[r + 1][c]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r + 1][c] = '-'
                if c - 1 in range(len(matrix)):
                    ch = matrix[r][c - 1]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r][c - 1] = '-'
                if c + 1 in range(len(matrix)):
                    ch = matrix[r][c + 1]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r][c + 1] = '-'
            santa_position = [r, c - 1]
            matrix[r][c-1] = 'S'
            matrix[r][c] = '-'
    elif command == 'right':
        if c + 1 in range(len(matrix)):
            char = matrix[r][c+1]
            if char == 'V':
                count_nice_kids += 1
                number_of_presents -= 1
            elif char == 'X':
                pass
            elif char == 'C':
                r, c = santa_position[0], santa_position[1]
                matrix[r][c] = '-'
                santa = [r - 1, c]
                r, c = santa[0], santa[1]

                if r - 1 in range(len(matrix)):
                    ch = matrix[r - 1][c]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r - 1][c] = '-'
                if r + 1 in range(len(matrix)):
                    ch = matrix[r + 1][c]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r + 1][c] = '-'
                if c - 1 in range(len(matrix)):
                    ch = matrix[r][c - 1]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r][c - 1] = '-'
                if c + 1 in range(len(matrix)):
                    ch = matrix[r][c + 1]
                    if ch == 'V':
                        count_nice_kids += 1
                    number_of_presents -= 1
                    matrix[r][c + 1] = '-'
            santa_position = [r, c + 1]
            matrix[r][c] = '-'
            matrix[r][c+1] = 'S'

    if number_of_presents <= 0:
        if count_nice_kids <= all_nice_kids:
            print("Santa ran out of presents!")
        break
    command = input()

print_matrix(matrix)
if count_nice_kids == all_nice_kids:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {all_nice_kids-count_nice_kids} nice kid/s.")

