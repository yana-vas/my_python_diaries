budget = float(input())
price_1_kg_flour = float(input())
price_1_pack_eggs = 0.75*price_1_kg_flour
price_1_lt_milk = price_1_kg_flour + 0.25*price_1_kg_flour

price_250_ml_milk = price_1_lt_milk/4
price_cozonacs = price_250_ml_milk + price_1_pack_eggs + price_1_kg_flour

start_budget = budget
colored_eggs_counter = 0
cozonacs_counter = 0
while not budget == start_budget % price_cozonacs:
    budget -= price_cozonacs
    colored_eggs_counter += 3
    cozonacs_counter += 1
    if cozonacs_counter % 3 == 0:
        colored_eggs_counter -= cozonacs_counter - 2

print(f"You made {cozonacs_counter} cozonacs! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")