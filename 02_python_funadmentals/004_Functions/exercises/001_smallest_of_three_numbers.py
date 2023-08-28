import sys

num_1_value = int(input())
num_2_value = int(input())
num_3_value = int(input())


def smallest_number(first_num, second_num, third_num):
    min_number = sys.maxsize
    if first_num < min_number:
        min_number = first_num
    if second_num < min_number:
        min_number = second_num
    if third_num < min_number:
        min_number = third_num
    return min_number


print(smallest_number(first_num=num_1_value, second_num=num_2_value, third_num=num_3_value))
