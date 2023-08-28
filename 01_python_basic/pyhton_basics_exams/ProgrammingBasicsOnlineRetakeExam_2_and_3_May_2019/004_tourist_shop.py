budget = float(input())
command = input()
product_counter = 0
all_sum = 0
left_money = budget
while command != "Stop":
    product = command
    price_of_product = float(input())
    product_counter += 1
    if product_counter % 3 == 0:
        price_of_product /= 2
    all_sum += price_of_product
    if price_of_product > left_money:
        needed_money = price_of_product - abs(left_money)
        print("You don'visible_trees have enough money!")
        print(f"You need {needed_money:.2f} leva!")
        break
    left_money -= price_of_product
    command = input()
if command == "Stop":
    print(f"You bought {product_counter} products for {all_sum:.2f} leva.")