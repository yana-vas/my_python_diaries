my_file = open("day_fouth_input_data.txt", 'r')
input_data = my_file.read()
input_data = input_data.split('\n')

counter = 0
pairs_counter = 0

# ----------- Second Part --------------

for line in input_data:
    first_part, second_part = line.split(',')
    start_first, end_first = list(map(int, first_part.split('-')))
    start_second, end_second = list(map(int, second_part.split('-')))
    first_list_numbers = [n for n in range(start_first, end_first+1)]
    second_list_numbers = [n for n in range(start_second, end_second+1)]
    overlaps = any(element in first_list_numbers for element in second_list_numbers)
    if overlaps:
        pairs_counter += 1
print(pairs_counter)

# ----------- First Part --------------

for line in input_data:
    first_part, second_part = line.split(',')
    start_first, end_first = list(map(int, first_part.split('-')))
    start_second, end_second = list(map(int, second_part.split('-')))
    if start_second <= start_first <= end_second and start_second <= end_first <= end_second:
        counter += 1
    elif start_first <= start_second <= end_first and start_first <= end_second <= end_first:
        counter += 1
print(counter)
