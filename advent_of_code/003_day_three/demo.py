import string

points = 0
letters = list(string.ascii_letters)

# ----------- Second Part --------------

my_file = open("input_data_third_day.txt", 'r')
input_data = my_file.read()
input_data = input_data.split('\n')
list_of_lists = [input_data[i:i+3] for i in range(0, len(input_data), 3)]

for my_list in list_of_lists:
    first_list = my_list[0]
    second_list = my_list[1]
    third_list = my_list[2]
    occurrences = set([])
    for char in first_list:
        second_num_occ = second_list.count(char)
        third_num_occ = third_list.count(char)
        if second_num_occ > 0 and third_num_occ > 0:
            occurrences.add(char)
    for c in occurrences:
        points += letters.index(c) + 1

# ----------- First Part --------------

with open('input_data_third_day.txt', 'r') as f:
    for line in f.readlines():

        second_half = line[len(line)//2:].strip()
        first_half = line[:len(line)//2]
        occurrences = set([])
        for char in first_half:
            num_occurrences = second_half.count(char)
            if num_occurrences > 0:
                occurrences.add(char)
        for c in occurrences:
            points += letters.index(c)+1
print(points)