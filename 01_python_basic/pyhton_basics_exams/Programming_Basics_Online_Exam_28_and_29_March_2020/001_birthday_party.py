rent = float(input())
cake_price = 20 * rent * 0.01
drinks_price = cake_price - 45 * cake_price * 0.01
animator_price = rent/3
all_sum = rent + cake_price + drinks_price + animator_price
print(f"{all_sum:.1f}")
