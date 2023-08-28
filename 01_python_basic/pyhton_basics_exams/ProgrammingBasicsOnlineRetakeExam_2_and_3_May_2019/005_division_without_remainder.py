n = int(input())
even_number_counter = 0
numbers_that_are_divisible_by_3_without_remainder = 0
numbers_that_are_divisible_by_4_without_remainder = 0
for i in range(n):
    current_number = int(input())
    if current_number % 2 == 0:
        even_number_counter += 1
        # print(f"the number {current_number} is divisible by 2")

    verification_for_division_by_3 = 0
    for index, character in enumerate(str(current_number)):
        verification_for_division_by_3 = int(verification_for_division_by_3)
        verification_for_division_by_3 += int(character)
    if int(verification_for_division_by_3) % 3 == 0:
        numbers_that_are_divisible_by_3_without_remainder += 1
        # print(f"the number {current_number} is divisible by 3")

    length = len(str(current_number))
    last_char = str(current_number)[length-1]
    second_last_char = str(current_number)[length-2]
    last_two_digit = second_last_char + last_char
    if int(last_two_digit) % 4 == 0:
        # print(f"the number {current_number} is divisible by 4")
        numbers_that_are_divisible_by_4_without_remainder += 1

# print(f"even numbers: {even_number_counter}")
# print(f"numbers that are divisible by 3 without remainder: {numbers_that_are_divisible_by_3_without_remainder}")
# print(f"numbers that are divisible by 4 without remainder: {numbers_that_are_divisible_by_4_without_remainder}")

p1 = even_number_counter / n * 100
p2 = numbers_that_are_divisible_by_3_without_remainder / n * 100
p3 = numbers_that_are_divisible_by_4_without_remainder / n * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
