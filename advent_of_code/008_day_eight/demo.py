def direction(dir):
    p = 0
    for n in dir:
        if n < tree:
            p += 1
        elif n >= tree:
            p += 1
            break
    return p


input_data = open("input_data.txt").read().split('\n')
edge_trees_sum = 0
edge_trees_sum += len(input_data[0])
edge_trees_sum += len(input_data[-1])
edge_trees_sum += (len(input_data) - 2) * 2
points = []
matrix = [[int(x) for x in list(el)] for el in input_data]
valid_numbers = []
for i in range(1, len(matrix) - 1):
    whole_row = matrix[i]
    row_trees = whole_row[1:-1]
    for j in range(len(row_trees)):
        tree = row_trees[j]
        col = j + 1
        row = i
        valid = False
        left = whole_row[:col]
        right = whole_row[col + 1:]
        column = []
        for el in matrix:
            column.append(el[col])
        up = column[:row]
        down = column[row + 1:]

        valid_left = all(i < tree for i in left)
        valid_right = all(i < tree for i in right)
        valid_up = all(i < tree for i in up)
        valid_down = all(i < tree for i in down)
        if valid_down or valid_up or valid_left or valid_right:
            valid = True
        if valid:
            valid_numbers.append(tree)

        p_up = direction(reversed(up))
        p_down = direction(down)
        p_left = direction(reversed(left))
        p_right = direction(right)
        points_sum = p_up * p_down * p_right * p_left
        points.append(points_sum)


all_trees = len(valid_numbers) + edge_trees_sum
print(all_trees)
print(max(points))
