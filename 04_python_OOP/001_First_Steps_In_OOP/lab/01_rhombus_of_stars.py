def print_row(size, r):
    print(' ' * (size - r), end='')
    for _ in range(1, r + 1):
        print('* ', end='')
    print()


n = int(input())

for row in range(1, n+1):
    print_row(n, row)
for row in range(n - 1, -1, -1):
    print_row(n, row)