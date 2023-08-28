excursion_price = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

all_toys = number_of_puzzles + number_of_talking_dolls + number_of_teddy_bears + number_of_minions + number_of_trucks
price_for_all_toys = (number_of_puzzles * 2.60) + (number_of_talking_dolls * 3) + (number_of_teddy_bears * 4.10) + (number_of_minions * 8.20) + (number_of_trucks * 2)

if all_toys >= 50:
    price_for_all_toys = price_for_all_toys - (price_for_all_toys * 0.25)
rent = price_for_all_toys * 0.1
price_for_all = price_for_all_toys - rent

if price_for_all >= excursion_price:
    left_money = price_for_all - excursion_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = abs(excursion_price - price_for_all)
    print(f"Not enough money! {needed_money:.02f} lv needed.")


