clothes = list(map(int, input().split(' ')))
rack_capacity = int(input())
racks = 1
sum = 0

for i in range(len(clothes)):
    if sum + clothes[-1] > rack_capacity:
        racks += 1
        sum = clothes.pop()
    elif sum + clothes[-1] == rack_capacity:
        sum = 0
        clothes.pop()
        if clothes:
            racks += 1
    else:
        sum += clothes.pop()
print(racks)