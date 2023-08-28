first_number_value = int(input())
second_number_value = int(input())


def factorial(num1, num2):
    first_number_factorial = 1
    second_number_factorial = 1
    for i in range(num1, 0, -1):
        first_number_factorial *= i
    for j in range(num2, 0, -1):
        second_number_factorial *= j
    print(f"{first_number_factorial / second_number_factorial:.2f}")


factorial(num1=first_number_value, num2=second_number_value)