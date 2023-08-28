input_data = input().split()
total_sum = 0
first_string = input_data[0]
second_string = input_data[1]

if len(first_string) == len(second_string):
    for i in range(len(first_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])
elif len(first_string) > len(second_string):
    for i in range(len(second_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    for j in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[j])
else:
    for i in range(len(first_string)):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    for j in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[j])
print(total_sum)
