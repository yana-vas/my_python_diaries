budget = float(input())
needed_fuel_lt = float(input())
day = input()
price_for_fuel = 2.1 * needed_fuel_lt
price_for_guide = 100
price_without_discount = price_for_guide + price_for_fuel
discount = 0

if day == "Saturday":
    discount = 10
elif day == "Sunday":
    discount = 20

needed_money = price_without_discount - (price_without_discount * discount)/100
if budget >= needed_money:
    left_money = budget - needed_money
    print(f"Safari time! Money left: {left_money:.2f} lv. ")
else:
    money_that_they_do_not_have_rn = abs(needed_money - budget)
    print(f"Not enough money! Money needed: {money_that_they_do_not_have_rn:.2f} lv.")
