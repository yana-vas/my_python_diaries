rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows):
    nums = [int(n) for n in input().split(' ')]
    matrix.append(nums)
for column_number in range(cols):
    column = []
    for line in matrix:
        column.append(int(line[column_number]))
    print(sum(column))
