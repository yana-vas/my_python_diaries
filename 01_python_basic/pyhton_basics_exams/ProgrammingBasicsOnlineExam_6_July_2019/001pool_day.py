import math

peoples = int(input())
tax_enter = float(input())
price_for_one_deck_chair = float(input())
price_for_one_umbrella = float(input())

tax_enter_for_all_peoples = tax_enter * peoples
price_for_umbrellas = math.ceil(peoples/2) * price_for_one_umbrella
price_for_deck_chairs = math.ceil((75*peoples)/100) * price_for_one_deck_chair

sum_for_all = tax_enter_for_all_peoples + price_for_umbrellas + price_for_deck_chairs

print(f"{sum_for_all:.2f} lv.")
