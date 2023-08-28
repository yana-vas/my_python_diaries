n = int(input())
numbers = []

positive = []
negative = []
even = []
odd = []
for i in range(n):
    current_integer = int(input())
    numbers.append(current_integer)
    if current_integer >= 0:
        positive.append(current_integer)
    else:
        negative.append(current_integer)
    if current_integer % 2 == 0 or current_integer == 0:
        even.append(current_integer)
    else:
        odd.append(current_integer)

command = input()

print(eval(command))