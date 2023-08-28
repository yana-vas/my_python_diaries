bought_food_kg = int(input())
command = input()
food_counter = 0
while command != "Adopted":
    food_gr = int(command)
    food_counter += food_gr
    command = input()
if food_counter <= bought_food_kg*1000:
    left_food = bought_food_kg*1000 - food_counter
    print(f"Food is enough! Leftovers: {left_food} grams.")
else:
    needed_food = food_counter - bought_food_kg*1000
    print(f"Food is not enough. You need {needed_food} grams more.")
