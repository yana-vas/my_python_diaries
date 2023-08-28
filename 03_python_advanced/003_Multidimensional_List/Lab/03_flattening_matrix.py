rows = int(input())
flattening_matrix = []

for _ in range(rows):
    nums = [int(x) for x in input().split(', ')]
    flattening_matrix.extend(nums)
print(flattening_matrix)