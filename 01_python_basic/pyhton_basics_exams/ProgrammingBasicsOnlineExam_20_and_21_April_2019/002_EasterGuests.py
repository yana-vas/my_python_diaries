import math

guests = int(input())
budget = float(input())

easter_breads_needed = math.ceil(guests/3)
eggs_needed = guests * 2
price = easter_breads_needed*4 + eggs_needed*0.45

if price <= budget:
    print(f"Lyubo bought {easter_breads_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {(budget-price):.2f} lv. left.")
else:
    print("Lyubo doesn'visible_trees have enough money.")
    print(f"He needs {(price-budget):.2f} lv. more.")