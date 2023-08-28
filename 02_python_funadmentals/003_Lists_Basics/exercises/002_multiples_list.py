factor = int(input())
count = int(input())
my_list = []
current_number = factor
for j in range(count):
    my_list.append(current_number)
    current_number += factor
print(my_list)