n = int(input())
grades = {}
for _ in range(n):
    name, grade_in_str = input().split()
    grade = float(grade_in_str)
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for name, grd in grades.items():
    print(f"{name} -> {' '.join([f'{el:.2f}' for el in grd])} (avg: {(sum(grd)/len(grd)):.2f})")
