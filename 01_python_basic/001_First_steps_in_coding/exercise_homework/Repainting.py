nylon_amount = int(input())
paint_amount_lt = int(input())
diluent_for_paint_lt = int(input())
needed_hours = int(input())

price_nylon = (nylon_amount + 2) * 1.50
price_paint = (paint_amount_lt + (paint_amount_lt * 0.1)) * 14.50
price_diluent = diluent_for_paint_lt * 5.00
price_bag = 0.40

sum = price_nylon + price_paint + price_diluent + price_bag

price_painters = (sum * 0.3) * 8

final_sum = sum + price_painters
print(final_sum)
