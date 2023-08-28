operation = input()
first_number_value = int(input())
second_number_value = int(input())


def calculator(operator, first_number, second_number):
    if operator == 'multiply':
        return first_number * second_number
    elif operator == 'divide':
        return int(first_number / second_number)
    elif operator == 'add':
        return first_number + second_number
    elif operator == 'subtract':
        return first_number - second_number


print(calculator(operator=operation, first_number=first_number_value, second_number=second_number_value))
