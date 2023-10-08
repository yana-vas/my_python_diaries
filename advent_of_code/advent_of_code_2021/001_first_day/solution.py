def num_increased(input_data):
    last_num = input_data[0]
    increased = []
    decreased = []

    for el in input_data:
        if el > last_num:
            increased.append(el)
        elif el < last_num:
            decreased.append(el)

        last_num = el

    return len(increased)


input_data = open("input_data.txt", 'r').read()
input_data = list(map(int, input_data.split('\n')))

print(num_increased(input_data))

window_sums = [sum(input_data[i:i+3]) for i in range(len(input_data) - 2)]  # Compute the sum of each window

print(num_increased(window_sums))
