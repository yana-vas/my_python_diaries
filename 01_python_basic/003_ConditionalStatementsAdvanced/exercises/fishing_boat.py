budget = int(input())
season = input()
number_of_fisherman = int(input())

rent_for_the_boat = 0

if season == "Spring":
    rent_for_the_boat = 3000
elif season == "Summer":
    rent_for_the_boat = 4200
elif season == "Autumn":
    rent_for_the_boat = 4200
elif season == "Winter":
    rent_for_the_boat = 2600

if number_of_fisherman <= 6:
    rent_for_the_boat = rent_for_the_boat - (rent_for_the_boat * 0.1)
elif 7 < number_of_fisherman <= 11:
    rent_for_the_boat = rent_for_the_boat - (rent_for_the_boat * 0.15)
elif number_of_fisherman > 12:
    rent_for_the_boat = rent_for_the_boat - (rent_for_the_boat * 0.25)

if season != "Autumn":
    if number_of_fisherman % 2 == 0:
        rent_for_the_boat = rent_for_the_boat - (rent_for_the_boat * 0.05)

if budget >= rent_for_the_boat:
    left_money = budget - rent_for_the_boat
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = abs(rent_for_the_boat - budget)
    print(f"Not enough money! You need {needed_money:.2f} leva.")