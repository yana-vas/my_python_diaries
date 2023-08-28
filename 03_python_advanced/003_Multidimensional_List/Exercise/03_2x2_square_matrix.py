rows, cols = [int(x) for x in input().split(' ')]
matrix = [input().split(' ') for _ in range(rows)]

special_matrix_count = 0

for row_index in range(rows-1):
    for col_index in range(cols-1):
        sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index+1],
                      matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]
        is_special_matrix = False
        for char in sub_matrix:
            if char == sub_matrix[0]:
                is_special_matrix = True
            else:
                is_special_matrix = False
                break
        if is_special_matrix:
            special_matrix_count += 1
print(special_matrix_count)