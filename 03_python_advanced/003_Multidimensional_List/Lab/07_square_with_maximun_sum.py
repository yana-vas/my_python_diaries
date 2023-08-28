rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

max_sum = -99999999999999999999999999999999
max_sum_matrix = []

for row_index in range(rows-1):
    for col_index in range(cols-1):
        sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index+1],
                      matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]

        curr_sum = sum(sub_matrix)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sum_matrix = sub_matrix.copy()
print(max_sum_matrix[0], max_sum_matrix[1])
print(max_sum_matrix[2], max_sum_matrix[3])
print(max_sum)