n = int(input())
odd = set()
even = set()

for row in range(1, n+1):
    name = input()
    ascii_value = 0
    for l in name:
        ascii_value += ord(l)
    ascii_value //= row
    if ascii_value % 2 == 0:
        even.add(ascii_value)
    else:
        odd.add(ascii_value)

if sum(even) == sum(odd):
    print(f"{', '.join(str(x) for x in odd.union(even))}")
elif sum(odd) > sum(even):
    print(f"{', '.join(str(x) for x in odd.difference(even))}")
elif sum(even) > sum(odd):
    print(f"{', '.join(str(x) for x in odd.symmetric_difference(even))}")
