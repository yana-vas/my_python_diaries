flour_kg_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_packets = int(input())
yeast_packets = int(input())

sugar = flour_kg_price - (flour_kg_price * 25/100)
eggs = flour_kg_price + (flour_kg_price * 10/100)
yeast = sugar - sugar * 80/100
price = flour_kg_price * flour_kg + sugar * sugar_kg + eggs*egg_packets + yeast*yeast_packets
print(f"{price:.2f}")

