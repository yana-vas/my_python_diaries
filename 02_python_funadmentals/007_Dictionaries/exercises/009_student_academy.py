report_card = {}
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())
    if name not in report_card:
        report_card[name] = []
    report_card[name].append(grade)

for name, grades in report_card.items():
    avg = sum(grades) / len(grades)
    if avg >= 4.5:
        print(f"{name} -> {avg:.2f}")
