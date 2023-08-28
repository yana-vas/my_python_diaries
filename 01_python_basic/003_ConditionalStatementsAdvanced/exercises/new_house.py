flower = input()
number_of_flowers = int(input())
budget = int(input())

price = 0
if flower == "Roses":
    price = 5 * number_of_flowers
    if number_of_flowers > 80:
        price = price - (price * 0.1)
elif flower == "Dahlias":
    price = 3.80 * number_of_flowers
    if number_of_flowers > 90:
        price = price - (price * 0.15)
elif flower == "Tulips":
    price = 2.80 * number_of_flowers
    if number_of_flowers > 80:
        price = price - (price * 0.15)
elif flower == "Narcissus":
    price = 3 * number_of_flowers
    if number_of_flowers < 120:
        price = (3 + 0.45) * number_of_flowers
elif flower == "Gladiolus":
    price = 2.50 * number_of_flowers
    if number_of_flowers < 80:
        price = (2.50 + 0.5) * number_of_flowers


# Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
if budget >= price:
    left_money = budget - price
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {left_money:.2f} leva left.")
else:
    needed_money = abs(price - budget)
    print(f"Not enough money, you need {needed_money:.2f} leva more.")