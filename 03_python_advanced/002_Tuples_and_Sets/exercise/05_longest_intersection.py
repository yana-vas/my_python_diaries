n = int(input())
longest = set()
for _ in range(n):
    first, second = input().split('-')
    first_start, first_end = [int(x) for x in first.split(',')]
    second_start, second_end = [int(x) for x in second.split(',')]

    first_intersection = set()
    second_intersection = set()
    for x in range(first_start, first_end + 1):
        first_intersection.add(x)
    for x in range(second_start, second_end + 1):
        second_intersection.add(x)
    intersection = first_intersection.intersection(second_intersection)
    if len(intersection) > len(longest):
        longest = intersection
print(f"Longest intersection is [{', '.join([str(x) for x in longest])}] with length {len(longest)}")
