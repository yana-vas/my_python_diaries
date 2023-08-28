strawberry_price_kg = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberry_price = strawberry_price_kg/2
orange_price = raspberry_price - (40 * raspberry_price * 0.01)
banana_price = raspberry_price - (raspberry_price * 80)/100
strawberry_price = strawberry_price_kg * strawberries_quantity
all_sum = (raspberry_price * raspberries_quantity) + (orange_price * oranges_quantity) + (banana_price*bananas_quantity) + strawberry_price

print(f"{all_sum:.2f}")

