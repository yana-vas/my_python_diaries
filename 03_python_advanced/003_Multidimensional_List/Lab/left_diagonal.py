n = int(input())
matrix = []

for _ in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

diagonal_left_sum = 0
row_index = 0
for col_index in range(n-1, -1, -1):
    diagonal_left_sum += matrix[row_index][col_index]
    row_index += 1

print(diagonal_left_sum)