command = input()
shopping_cart = {}
while command != 'buy':
    command = command.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in shopping_cart:
        shopping_cart[product] = {}
        shopping_cart[product]["quantity"] = 0
    shopping_cart[product]["price"] = price
    shopping_cart[product]["quantity"] += quantity
    command = input()
for key, value in shopping_cart.items():
    total_price = shopping_cart[key]['quantity'] * shopping_cart[key]['price']
    print(f"{key} -> {total_price:.2f}")
