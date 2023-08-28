numbers = [int(num) for num in input().split(', ')]
positive_numbers = filter(lambda num: num >= 0, numbers)
negative_numbers = filter(lambda num: num < 0, numbers)
even_numbers = filter(lambda num: num % 2 == 0, numbers)
odd_numbers = filter(lambda num: num % 2 != 0, numbers)

print(f"Positive: {', '.join(str(number) for number in positive_numbers)}")
print(f"Negative: {', '.join(str(number) for number in negative_numbers)}")
print(f"Even: {', '.join(str(number) for number in even_numbers)}")
print(f"Odd: {', '.join(str(number) for number in odd_numbers)}")
