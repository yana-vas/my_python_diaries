budget = float(input())
number_of_serials = int(input())
starting_budget = budget
price_for_all = 0.0
for i in range(number_of_serials):
    serial_name = input()
    price_for_the_serial = float(input())
    if serial_name == "Thrones":
        price_for_the_serial -= 50 * price_for_the_serial / 100
    elif serial_name == "Lucifer":
        price_for_the_serial -= 40 * price_for_the_serial / 100
    elif serial_name == "Protector":
        price_for_the_serial -= 30 * price_for_the_serial / 100
    elif serial_name == "TotalDrama":
        price_for_the_serial -= 20 * price_for_the_serial / 100
    elif serial_name == "Area":
        price_for_the_serial -= 10 * price_for_the_serial / 100
    price_for_all += price_for_the_serial
    budget -= price_for_the_serial
if budget >= 0:
    print(f"You bought all the series and left with {abs(starting_budget - price_for_all):.2f} lv.")
else:
    needed_money = price_for_all - starting_budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")
