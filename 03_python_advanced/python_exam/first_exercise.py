from collections import deque

milligrams_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))
coffeine_limit = 300
drank_coffeine = 0
initial = 0
while energy_drinks and milligrams_caffeine:
    drink = milligrams_caffeine[-1] * energy_drinks[0]
    if drink+drank_coffeine <= 300:
        milligrams_caffeine.pop()
        energy_drinks.popleft()
        drank_coffeine += drink
    else:
        milligrams_caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())
        if drank_coffeine - 30 < 0:
            drank_coffeine = 0
        else:
            drank_coffeine -= 30
if len(energy_drinks) > 0:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn'visible_trees exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {drank_coffeine} mg caffeine.")
