number_of_cities = int(input())
total_profit = 0
for city_counter in range(1, number_of_cities+1):
    name_city = input()
    earned_money = float(input())
    expenses = float(input())
    if city_counter % 5 == 0:
        earned_money -= earned_money * 0.1
    elif city_counter % 3 == 0:
        expenses += expenses * 0.5
    current_profit = earned_money - expenses
    total_profit += current_profit
    print(f"In {name_city} Burger Bus earned {current_profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
