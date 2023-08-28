rows, cols = [int(x) for x in input().split(' ')]
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]


max_sum = -99999999999999999999999999999999
max_sum_matrix = []

for row_index in range(rows-2):
    for col_index in range(cols-2):
        sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index+1], matrix[row_index][col_index+2],
                      matrix[row_index+1][col_index], matrix[row_index+1][col_index+1], matrix[row_index+1][col_index+2],
                      matrix[row_index+2][col_index], matrix[row_index+2][col_index+1], matrix[row_index+2][col_index+2]]

        curr_sum = sum(sub_matrix)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sum_matrix = sub_matrix.copy()
print(f'Sum = {max_sum}')
print(max_sum_matrix[0], max_sum_matrix[1], max_sum_matrix[2])
print(max_sum_matrix[3], max_sum_matrix[4], max_sum_matrix[5])
print(max_sum_matrix[6], max_sum_matrix[7], max_sum_matrix[8])
