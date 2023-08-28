number_of_numbers = int(input())

left_sum = 0
for i in range(number_of_numbers):
    value_left = int(input())
    left_sum += value_left
right_sum = 0
for i in range(number_of_numbers):
    value_right = int(input())
    right_sum += value_right

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs((left_sum - right_sum))
    print(f"No, diff = {difference}")