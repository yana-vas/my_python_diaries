minutes = int(input())
number_of_walks_daily = int(input())
calories = int(input())
burnt_calories = minutes * number_of_walks_daily * 5
if burnt_calories >= 50*calories/100:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burnt_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burnt_calories}.")
