number = int(input())
is_special = False
current_digit = ""
current_number_sum = 0
for current_number in range(1, number + 1):
    for digit in range(len(str(current_number))):
        number_in_string = str(current_number)
        current_digit = number_in_string[digit]
        current_number_sum += int(current_digit)
    if int(current_number_sum) == 5 or int(current_number_sum) == 7 or int(current_number_sum) == 11:
        is_special = True
    if is_special:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")
    is_special = False
    current_digit = 0
    current_number_sum = 0