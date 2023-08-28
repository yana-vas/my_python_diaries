import sys

number = int(input())
max_num = -sys.maxsize
sum_numbers = 0

for i in range(number):
    value = int(input())
    if value > max_num:
        max_num = value
    sum_numbers += value
if max_num == sum_numbers - max_num:
    half_sum = sum_numbers//2
    print("Yes")
    print(f"Sum = {half_sum}")
else:
    print("No")
    sum_numbers = sum_numbers - max_num
    print(f"Diff = {abs(max_num - sum_numbers)}")
