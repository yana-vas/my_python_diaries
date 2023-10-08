##Taking examples of two python lists.

##Take examples of two lists.

list1 = [2,4,0,7,6]
list2 = [1,0,9,7,6]

##the statement for condition is.

check = any(element in list2 for element in list1)


# Directons in matrix - UP DOWN LEFT RIGHT (see more on advent_of_code_2022/008_day_eight/theory.py)

#         for x in range(c - 1, -1, -1):
#             L += 1
#             if grid[r][x] >= k:
#                 break
#
#         for x in range(c + 1, len(grid[r])):
#             R += 1
#             if grid[r][x] >= k:
#                 break
#
#         for x in range(r - 1, -1, -1):
#             U += 1
#             if grid[x][c] >= k:
#                 break
#
#         for x in range(r + 1, len(grid[r])):
#             D += 1
#             if grid[x][c] >= k:
#                 break