searched_strings = input().split(', ')
input_strings = input().split(', ')
filtered_string = list()
# filtered_string = [current_searched_string for current_searched_string in searched_strings
#                    for current_string in input_strings if current_searched_string in current_string
#                    if current_searched_string not in filtered_string]
# filtered_string = list(set(filtered_string))
for current_searched_string in searched_strings:
    for current_string in input_strings:
        if current_searched_string in current_string:
            if current_searched_string not in filtered_string:
                filtered_string.append(current_searched_string)
print(filtered_string)
