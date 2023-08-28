num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(third_num):
    return sum_numbers(first_num=num_1, second_num=num_2) - third_num


def add_and_subtract(first_number, second_number, third_number):
    return subtract(third_num=third_number)


print(add_and_subtract(first_number=num_1, second_number=num_2, third_number=num_3))
