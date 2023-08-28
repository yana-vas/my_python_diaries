wanted_profit = float(input())
command = input()
summ = 0
while command != "Party!":
    number_of_drinks = int(input())
    price = len(command) * number_of_drinks
    if price % 2 != 0:
        price -= (25*price)/100
    summ += price
    if summ >= wanted_profit:
        break
    command = input()
if command == "Party!":
    needed_money = wanted_profit - summ
    print(f"We need {needed_money:.2f} leva more.")
else:
    print("Target acquired.")
print(f"Club income - {summ:.2f} leva.")
