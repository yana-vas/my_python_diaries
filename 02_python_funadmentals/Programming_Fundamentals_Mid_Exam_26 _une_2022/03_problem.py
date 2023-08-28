price_ratings = [int(x) for x in input().split(', ')]
entry_point = int(input())
type_of_items = input()
index = entry_point

position = ''
left = price_ratings[:entry_point-1]
right = price_ratings[entry_point+1:]
left_sum = 0
right_sum = 0
special_number = price_ratings[entry_point]
if type_of_items == 'cheap':
    left_sum = [num for num in left if num < special_number]
    right_sum = [num for num in right if num < special_number]
else:
    left_sum = [num for num in left if num >= special_number]
    right_sum = [num for num in right if num >= special_number]
if sum(right_sum) > sum(left_sum):
    print(f"Right - {sum(right_sum)}")
else:
    print(f"Left - {sum(left_sum)}")