quantity = int(input())
days = int(input())

ornament_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights = 15
budget = 0
spirit = 0
for days_counter in range(1, days+1):
    if days_counter % 11 == 0:
        quantity += 2
    if days_counter % 2 == 0:
        budget += ornament_price * quantity
        spirit += 5
    if days_counter % 10 == 0:
        if days == days_counter:
            spirit -= 30
        spirit -= 20
        budget += tree_lights + tree_garlands_price + tree_skirt_price
    if days_counter % 3 == 0:
        budget += (tree_skirt_price * quantity) + (tree_garlands_price * quantity)
        spirit += 13
    if days_counter % 5 == 0:
        budget += tree_lights * quantity
        spirit += 17
        if days_counter % 3 == 0:
            spirit += 30

    days_counter += 1
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
