number = int(input())

bonus = 0
if number <= 100:
    bonus = 5
elif 1000 > number > 100:
    bonus = number * 0.2
else:
    bonus = number * 0.1

if number % 2 == 0:
    bonus += 1
if number % 10 == 5:
    bonus += 2

print(bonus)
print(bonus + number)