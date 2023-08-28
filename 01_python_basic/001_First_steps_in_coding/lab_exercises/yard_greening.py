square_meters = float(input())
price_without_discount = square_meters * 7.61
discount = price_without_discount * 0.18
price = price_without_discount - discount
print(f"The final price is: {price} lv.")
print(f"The discount is: {discount} lv.")