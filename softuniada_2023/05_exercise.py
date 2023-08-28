import sys

numbers = [int(n) for n in input().split()]
numbers = sorted(numbers, key=int)[::-1]

first_value_num = []
nums_sort = []
while numbers:
    biggest_number = -sys.maxsize
    biggest_number_first_digit = -sys.maxsize
    for num in numbers:
        if int(str(num)[0]) > biggest_number_first_digit:
            biggest_number = num
            biggest_number_first_digit = int(str(num)[0])
    numbers.remove(biggest_number)
    nums_sort.append(biggest_number)

# last_fixes_numbers = []
# for number in nums_sort:
#     if '0' in str(number):
#         nums_sort.remove(number)
#         nums_sort.append(number)
i = 0
c = 0
while i < len(nums_sort):
    if c >= len(nums_sort):
        break
    number = nums_sort[i]
    c += 1
    if '0' in str(number):
        nums_sort.remove(number)
        nums_sort.append(number)
        continue
    i += 1

nums_sort = [str(x) for x in nums_sort]
print(''.join(nums_sort))

