trunk_capacity = float(input())
command = input()
used_space_counter = 0
suitcase_counter = 0
while command != "End":
    suitcase_volume = float(command)
    used_space_counter += suitcase_volume
    if used_space_counter >= trunk_capacity:
        break
    suitcase_counter += 1
    if suitcase_counter % 3 == 0:
        suitcase_volume += 10 * suitcase_volume / 100
    command = input()
if command == "End":
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {suitcase_counter} suitcases loaded.")