width_apartment = int(input())
length_apartment = int(input())
height_apartment = int(input())
free_space = width_apartment * length_apartment * height_apartment
used_space = 0
cubic_meters_apartment = free_space
while free_space > 0:
    boxes_or_command = input()
    if boxes_or_command == "Done":
        break
    else:
        boxes_or_command = int(boxes_or_command)
        used_space += boxes_or_command
        free_space -= boxes_or_command
if free_space <= 0:
    needed_space = abs(cubic_meters_apartment - used_space)
    print(f"No more free space! You need {needed_space} Cubic meters more.")
if boxes_or_command == "Done":
    left_free_space = cubic_meters_apartment - used_space
    print(f"{left_free_space} Cubic meters left.")