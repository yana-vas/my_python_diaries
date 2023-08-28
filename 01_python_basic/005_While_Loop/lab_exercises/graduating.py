name = input()

year = 1
sum = 0
excluded = 0
while year <= 12:
    if excluded > 1:
        break

    grade = float(input())

    if grade < 4.00:
        excluded += 1
        continue
    sum += grade
    year += 1

if excluded > 1:
    print(f"{name} has been excluded at {year} grade")
else:
    average = sum / 12
    print(f"{name} graduated. Average grade: {average:.2f}")

