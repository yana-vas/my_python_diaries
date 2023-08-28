input_data = input().split()


def position(alphabet):
    return ord(alphabet) - 96


total_sum = 0
for element in input_data:
    first_letter = element[0]
    last_letter = element[-1]
    number = float(element[1:-1])
    curr_sum = 0
    if first_letter.isupper():
        curr_sum += number/position(first_letter.lower())
    else:
        curr_sum += number * position(first_letter)

    if last_letter.isupper():
        curr_sum -= position(last_letter.lower())
    else:
        curr_sum += position(last_letter)
    total_sum += curr_sum
print(f'{total_sum:.2f}')