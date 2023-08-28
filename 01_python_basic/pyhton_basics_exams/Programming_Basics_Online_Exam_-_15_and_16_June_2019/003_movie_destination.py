budget = float(input())
destination = input()
season = input()
days = int(input())

price = days
if season == "Winter":
    if destination == "Dubai":
        price *= 45000
        price -= 30 * price / 100
    elif destination == "Sofia":
        price *= 17000
        price += 25 * price / 100
    elif destination == "London":
        price *= 24000
elif season == "Summer":
    if destination == "Dubai":
        price *= 40000
        price -= 30 * price / 100
    elif destination == "Sofia":
        price *= 12500
        price += 25 * price / 100
    elif destination == "London":
        price *= 20250
if price <= budget:
    left_money = budget - price
    print(f"The budget for the movie is enough! We have {left_money:.2f} leva left!")
else:
    needed_money = price - budget
    print(f"The director needs {needed_money:.2f} leva more!")

