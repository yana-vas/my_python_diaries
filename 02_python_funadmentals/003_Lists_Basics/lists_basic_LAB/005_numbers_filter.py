n = int(input())
numbers = []
for i in range(n):
    current_integer = int(input())
    numbers.append(current_integer)

command = input()
filtered = []
if command == "even":
    for current_number in numbers:
        if current_number % 2 == 0 or current_number == 0:
            filtered.append(current_number)
elif command == "odd":
    for current_number in numbers:
        if current_number % 2 != 0:
            filtered.append(current_number)
elif command == "negative":
    for current_number in numbers:
        if current_number < 0:
            filtered.append(current_number)
elif command == "positive":
    for current_number in numbers:
        if current_number >= 0:
            filtered.append(current_number)
print(filtered)