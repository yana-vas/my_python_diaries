people = int(input())
lift = [int(num) for num in input().split()]
for i in range(len(lift)):
    if people < 4 - lift[i]:
        can_load = people
    else:
        can_load = 4 - lift[i]
    # can_load = min(4 - lift[i], people)
    lift[i] += can_load
    people -= can_load
has_empty_spots = lift[-1] < 4
lift = list(map(str, lift))
if has_empty_spots and people == 0:
    print("The lift has empty spots!")
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
print(f"{' '.join(lift)}")