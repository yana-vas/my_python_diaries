number_of_lines = int(input())
water_tank_capacity = 255
liters_of_water = 0
for i in range(number_of_lines):
    current_liters_of_water = int(input())
    liters_of_water += current_liters_of_water
    if liters_of_water > water_tank_capacity:
        print("Insufficient capacity!")
        liters_of_water -= current_liters_of_water
print(liters_of_water)
