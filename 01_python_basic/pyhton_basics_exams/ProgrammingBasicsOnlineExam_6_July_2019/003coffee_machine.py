drink = input()
sugar = input()
number_of_drinks = int(input())

price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = 0.90 * number_of_drinks
    elif sugar == "Normal":
        price = 1.0 * number_of_drinks
    elif sugar == "Extra":
        price = 1.20 * number_of_drinks
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1.0 * number_of_drinks
    elif sugar == "Normal":
        price = 1.20 * number_of_drinks
    elif sugar == "Extra":
        price = 1.60 * number_of_drinks
elif drink == "Tea":
    if sugar == "Without":
        price = 0.50 * number_of_drinks
    elif sugar == "Normal":
        price = 0.60 * number_of_drinks
    elif sugar == "Extra":
        price = 0.70 * number_of_drinks

if sugar == "Without":
    price -= 35*price/100
if drink == "Espresso" and number_of_drinks >= 5:
    price -= 25*price/100
if price > 15:
    price -= 20*price/100
print(f"You bought {number_of_drinks} cups of {drink} for {price:.2f} lv.")
