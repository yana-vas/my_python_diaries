matrix = [line.split(' ') for line in input().split('|')][::-1]
for row in matrix:
    for char in row:
        if char != '':
            print(char, end=' ')
