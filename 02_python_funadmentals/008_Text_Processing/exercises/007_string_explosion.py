my_str = input()
filtered_string = ''
strength = 0
for i in range(len(my_str)):
    char = my_str[i]
    if strength > 0 and char != '>':
        strength -= 1
    else:
        if char == '>':
            strength += int(my_str[i + 1])
        filtered_string += char

print(filtered_string)


