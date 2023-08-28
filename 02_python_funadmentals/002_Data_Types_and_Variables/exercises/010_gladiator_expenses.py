lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_counter = 0
sword_counter = 0
shield_counter = 0

broken_shield_counter = 0
expenses = 0
for current_lost_game in range(1, lost_fights_count+1):
    if current_lost_game % 2 == 0:
        helmet_counter += 1
    if current_lost_game % 3 == 0:
        sword_counter += 1
    if current_lost_game % 2 == 0 and current_lost_game % 3 == 0:
        shield_counter += 1
        broken_shield_counter += 1
expenses = (helmet_counter * helmet_price) + (sword_counter * sword_price) + (shield_counter * shield_price) + \
           ((broken_shield_counter // 2) * armor_price)

print(f"Gladiator expenses: {expenses:.2f} aureus")

