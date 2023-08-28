needed_money = float(input())
current_money = float(input())

days = 0
days_spending_money = 0

while current_money < needed_money and days_spending_money < 5:
    command = input()
    money = float(input())
    if command == "spend":
        current_money -= money
        if current_money < 0:
            current_money = 0
        days_spending_money += 1
    elif command == "save":
        current_money += money
        days_spending_money = 0
    days += 1
if days_spending_money == 5:
    print("You can'visible_trees save the money.")
    print(f"{days}")
if current_money >= needed_money:
    print(f"You saved the money for {days} days.")
