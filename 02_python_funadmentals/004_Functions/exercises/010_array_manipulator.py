import sys

numbers_list = input().split(" ")


def exchange(numbers, i):
    first_part = numbers[:i + 1]
    second_part = numbers[i + 1:]
    return second_part + first_part


def max_even(numbers):
    is_max_even_num = False
    max_num_index = 0
    max_number = -sys.maxsize
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 == 0:
            is_max_even_num = True
            if int(numbers[i]) >= max_number:
                max_num_index = i
                max_number = int(numbers[i])
    if not is_max_even_num:
        return "No matches"
    else:
        if int(max_number) % 2 == 0:
            return max_num_index


def max_odd(numbers):
    is_max_odd_num = False
    max_num_index = 0
    max_number = -sys.maxsize
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 != 0:
            is_max_odd_num = True
            if int(numbers[i]) >= max_number:
                max_num_index = i
                max_number = int(numbers[i])
    if not is_max_odd_num:
        return "No matches"
    else:
        if int(max_number) % 2 != 0:
            return max_num_index


def min_odd(numbers):
    is_min_odd_num = False
    min_num = sys.maxsize
    min_num_index = 0
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 != 0:
            is_min_odd_num = True
            if int(numbers[i]) <= min_num:
                min_num_index = i
                min_num = int(numbers[i])
    if not is_min_odd_num:
        return "No matches"
    else:
        if int(min_num) % 2 != 0:
            return min_num_index


def min_even(numbers):
    is_min_even_num = False
    min_num = sys.maxsize
    min_num_index = 0
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 == 0:
            is_min_even_num = True
            if int(numbers[i]) <= min_num:
                min_num_index = i
                min_num = int(numbers[i])
    if not is_min_even_num:
        return "No matches"
    else:
        if int(min_num) % 2 == 0:
            return min_num_index


def first_count_even_or_odd(numbers, count, even_or_odd):
    if even_or_odd == 'even':
        even_numbers = []
        first_even_numbers = []
        for element in numbers:
            if int(element) % 2 == 0:
                even_numbers.append(int(element))
        if count > len(numbers):
            return "Invalid count"
        else:
            if count > len(even_numbers):
                count = len(even_numbers)
            for i in range(count):
                first_even_numbers.append(int(even_numbers[i]))
            if len(first_even_numbers) == 0:
                return '[]'
            else:
                first_even_numbers = [int(i) for i in first_even_numbers]
                return first_even_numbers
    else:
        if even_or_odd == 'odd':
            odd_numbers = []
            first_odd_numbers = []
            for element in numbers:
                if int(element) % 2 != 0:
                    odd_numbers.append(int(element))
            if count > len(numbers):
                return "Invalid count"
            else:
                if count > len(odd_numbers):
                    count = len(odd_numbers)
                for i in range(count):
                    first_odd_numbers.append(int(odd_numbers[i]))

                if len(first_odd_numbers) == 0:
                    return '[]'
                else:
                    first_odd_numbers = [int(i) for i in first_odd_numbers]
                    return first_odd_numbers


def last_count_even_or_odd(numbers, count, even_or_odd):
    if even_or_odd == 'even':
        even_numbers = []
        last_even_numbers = []
        for element in numbers:
            if int(element) % 2 == 0:
                even_numbers.append(int(element))
        if count > len(numbers):
            return "Invalid count"
        else:
            if len(last_even_numbers) == 0:
                return '[]'
            else:
                for i in range(1, count + 1):
                    last_even_numbers.append(even_numbers[-i])
                last_even_numbers.reverse()
                last_even_numbers = [int(i) for i in last_even_numbers]
                return last_even_numbers
    else:
        odd_numbers = []
        last_odd_numbers = []
        for element in numbers:
            if int(element) % 2 != 0:
                odd_numbers.append(int(element))
        if count > len(numbers):
            return "Invalid count"
        else:
            if count > len(odd_numbers):
                count = len(odd_numbers)
            for i in range(1, count + 1):
                last_odd_numbers.append(odd_numbers[-i])
            if len(last_odd_numbers) == 0:
                return '[]'
            else:
                last_odd_numbers.reverse()
                last_odd_numbers = [int(i) for i in last_odd_numbers]
                return last_odd_numbers


numbers_list = [int(i) for i in numbers_list]
command = input()
while command != 'end':
    command_list = command.split(' ')
    index = 0
    if command_list[0] == 'exchange':
        index = int(command_list[1])
        if len(numbers_list) > index >= 0:
            numbers_list = exchange(numbers_list, index)
        else:
            print('Invalid index')
    elif command_list[0] == 'max':
        if command_list[1] == 'even':
            print(max_even(numbers=numbers_list))
        else:
            print(max_odd(numbers=numbers_list))
    elif command_list[0] == 'min':
        if command_list[1] == 'even':
            print(min_even(numbers=numbers_list))
        else:
            print(min_odd(numbers=numbers_list))
    elif command_list[0] == 'first':
        print(first_count_even_or_odd(numbers=numbers_list, count=int(command_list[1]), even_or_odd=command_list[2]))
    elif command_list[0] == 'last':
        print(last_count_even_or_odd(numbers=numbers_list, count=int(command_list[1]), even_or_odd=command_list[2]))
    command = input()

print(numbers_list)
