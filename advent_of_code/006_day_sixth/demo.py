from collections import deque

input_data = deque(list(open("sixth_day_input_data.txt", 'r').read()))

start_of_packet_marker_found = False
index = 0
while not start_of_packet_marker_found:
    curr_elements = list(input_data)[0:14]  # за първата част заменяме 14 с 4
    my_set = list(set(curr_elements))
    if len(curr_elements) == len(my_set):
        start_of_packet_marker_found = True
        break
    input_data.popleft()
    index += 1
print(index+14)  # за първата част заменяме 14 с 4