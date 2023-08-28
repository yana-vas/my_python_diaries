movie_budget = float(input())
number_of_extras = int(input())
price_for_clothing_of_one_extra = float(input())

# Декорът за филма е на стойност 10% от бюджета.
# При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.

decor = movie_budget * 0.1
if number_of_extras > 150:
    price_for_clothing_of_one_extra = price_for_clothing_of_one_extra - (price_for_clothing_of_one_extra * 0.1)
price_for_clothing = price_for_clothing_of_one_extra * number_of_extras

sum = decor + price_for_clothing

if sum > movie_budget:
    needed_money = abs(sum - movie_budget)
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
else:
    left_money = movie_budget - sum
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")


