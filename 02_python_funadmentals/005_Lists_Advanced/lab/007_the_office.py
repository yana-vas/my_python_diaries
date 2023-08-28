employees_happiness = input().split(' ')
happiness_improvement_factor = int(input())
employees_happiness = list(map(int, employees_happiness))
employees_happiness = list(map(lambda happiness: happiness*2, employees_happiness))
avg_happiness = sum(employees_happiness) / len(employees_happiness)
happy_employees = [happy for happy in employees_happiness if happy >= avg_happiness]
if len(happy_employees) >= len(employees_happiness)//2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")
