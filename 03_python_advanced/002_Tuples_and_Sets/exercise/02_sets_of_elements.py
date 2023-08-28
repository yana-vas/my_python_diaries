n, m = list(map(lambda x: int(x), input().split()))  # the lengths of two separate sets

set_n = set()
set_m = set()

for _ in range(n):
    num_n = int(input())
    set_n.add(num_n)

for _ in range(m):
    num_m = int(input())
    set_m.add(num_m)

common_elements = set_n.intersection(set_m)
for num in common_elements:
    print(num)