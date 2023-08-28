input_data = input()
unique_elements = []
rage_message = ''
cur_string = ''
for i in range(len(input_data)):
    char = input_data[i]

    if not char.isdigit():
        if char.isalpha():
            char = char.upper()
        cur_string += char
        if char not in unique_elements:
            unique_elements.append(char)
    else:
        if i != len(input_data)-1 and input_data[i+1].isdigit():
            char += input_data[i+1]
        for i in range(int(char)):
            rage_message += cur_string
        cur_string = ''
print(f'Unique symbols used: {len(unique_elements)}')
print(rage_message)