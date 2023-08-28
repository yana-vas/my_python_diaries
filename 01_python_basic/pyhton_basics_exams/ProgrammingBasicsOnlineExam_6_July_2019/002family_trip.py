budget = float(input())
number_of_overnight_stays = int(input())
price_for_one_night = float(input())
percent_for_additional_costs = int(input())

if number_of_overnight_stays > 7:
    price_for_one_night -= (price_for_one_night*5)/100
additional_costs = percent_for_additional_costs*budget/100
price_for_the_stay = price_for_one_night * number_of_overnight_stays

sum = price_for_the_stay + additional_costs
if sum <= budget:
    remaining_money = budget - sum
    print(f"Ivanovi will be left with {remaining_money:.2f} leva after vacation.")
else:
    needed_money = abs(sum - budget)
    print(f"{needed_money:.2f} leva needed.")