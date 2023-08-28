level_of_fire = input().split("#")
amount_of_water = int(input())
cells = []
effort = 0
total_fire = 0
for index in range(len(level_of_fire)):
    if amount_of_water < 1:
        break
    current_level_of_fire = level_of_fire[index].split(" = ")
    type_of_fire = current_level_of_fire[0]
    value_of_cell = int(current_level_of_fire[1])
    if amount_of_water < value_of_cell:
        continue
    if type_of_fire == "High":
        if 81 <= value_of_cell <= 125:
            amount_of_water -= value_of_cell
            effort += 0.25*value_of_cell
            cells.append(value_of_cell)
    elif type_of_fire == "Medium":
        if 51 <= value_of_cell <= 80:
            amount_of_water -= value_of_cell
            effort += 0.25 * value_of_cell
            cells.append(value_of_cell)
    elif type_of_fire == "Low":
        if 1 <= value_of_cell <= 50:
            amount_of_water -= value_of_cell
            effort += 0.25 * value_of_cell
            cells.append(value_of_cell)

print("Cells:")
for cell in cells:
    print(f" - {cell}")
    total_fire += cell
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
