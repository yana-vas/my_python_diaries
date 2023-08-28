n = int(input())  # square matrix - n = row = column
matrix = []

for _ in range(n):
    line = list(input())
    matrix.append(line)

searched_char = input()
char_found = False
for i in range(n):
    for j in range(n):
        char = matrix[i][j]
        if char == searched_char:
            char_found = True
            print(f'({i}, {j})')
            break
    if char_found:
        break

if not char_found:
    print(f"{searched_char} does not occur in the matrix")
