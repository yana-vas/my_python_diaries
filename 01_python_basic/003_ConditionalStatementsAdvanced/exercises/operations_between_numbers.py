number1 = int(input())
number2 = int(input())
operator = input()

result = 0
even_or_odd = ""
if operator == "+":
    result = number1 + number2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
elif operator == "-":
    result = number1 - number2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
elif operator == "*":
    result = number1 * number2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
elif operator == "/":
    if number2 == 0:
        print(f"Cannot divide {number2} by zero")
    else:
        result = number1 / number2
        print(f"{number1} / {number2} = {result:.2f}")
elif operator == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 % number2
        print(f"{number1} % {number2} = {result}")

if operator == "+" or operator == "-" or operator == "*":
    print(f"{number1} {operator} {number2} = {result} - {even_or_odd}")