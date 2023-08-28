number_of_numbers = int(input())

even_numbers_sum = 0
odd_numbers_sum = 0
for i in range(number_of_numbers):
    value = int(input())
    if i % 2 == 0:
        even_numbers_sum += value
    else:
        odd_numbers_sum += value


if even_numbers_sum == odd_numbers_sum:
    print("Yes")
    print(f"Sum = {even_numbers_sum}")
else:
    difference = abs(even_numbers_sum - odd_numbers_sum)
    print("No")
    print(f"Diff = {difference}")