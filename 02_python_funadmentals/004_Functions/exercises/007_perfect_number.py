import math

number_value = int(input())


def perfect_number(num):
    current_numbers_sum = 0
    if num % 2 == 0:
        current_number = num//2
        while current_number >= 1:
            current_numbers_sum += math.ceil(current_number)
            if current_number == 1:
                break
            current_number = math.ceil(current_number / 2)
    if current_numbers_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number(num=number_value))
