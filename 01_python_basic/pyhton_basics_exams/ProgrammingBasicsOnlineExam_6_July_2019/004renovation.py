import math

wall_height = int(input())
wall_width = int(input())
percent_no_painting_area = int(input())

area = math.ceil(wall_height * wall_width * 4) - (math.ceil(wall_height * wall_width * 4)*percent_no_painting_area)/100
command = input()
while command != "Tired!":
    paint_lt = int(command)
    area -= paint_lt
    if area <= 0:
        break
    command = input()
if command == "Tired!":
    print(f"{area:.0f} quadratic m left.")
elif area < 0:
    print(f"All walls are painted and you have {abs(area):.0f} l paint left!")
else:
    print("All walls are painted! Great job, Pesho!")

