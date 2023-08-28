n = int(input())
names = set()
for _ in range(n):
    current_name = input()
    names.add(current_name)

for name in names:
    print(name)