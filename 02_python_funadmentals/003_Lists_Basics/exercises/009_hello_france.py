items = input().split("|")
budget = float(input())
earned_money = []
profit = 0
for index in range(len(items)):
    current_item = items[index].split("->")
    current_type = current_item[0]
    current_price = float(current_item[1])
    if budget < current_price:
        continue
    if current_type == "Clothes":
        if current_price <= 50.00:
            budget -= current_price
        else:
            continue
    elif current_type == "Shoes":
        if current_price <= 35.00:
            budget -= current_price
        else:
            continue
    elif current_type == "Accessories":
        if current_price <= 20.50:
            budget -= current_price
        else:
            continue
    profit += current_price * 0.40
    earned_money.append(current_price + current_price * 0.40)

total_money = budget
for element in earned_money:
    print(f"{element:.2f}", end=" ")
    total_money += float(element)
print(f"\nProfit: {profit:.2f}")
if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

