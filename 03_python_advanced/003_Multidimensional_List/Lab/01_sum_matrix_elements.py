rows, columns = [int(x) for x in input().split(', ')]
matrix = []
result = 0

for _ in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    result += sum(numbers)
    matrix.append(numbers)
print(result)
print(matrix)