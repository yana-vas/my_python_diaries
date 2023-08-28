easter_breads = int(input())
egg_packs = int(input())
biscuits_kg = int(input())

price = 3.20*easter_breads + 4.35*egg_packs + 5.40*biscuits_kg + (0.15*12) * egg_packs
print(f"{price:.2f}")