n = int(input())
matrix = []

for _ in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

diagonal_sum = 0
for index in range(n):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)

