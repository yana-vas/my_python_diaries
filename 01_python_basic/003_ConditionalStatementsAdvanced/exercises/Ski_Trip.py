days = int(input())
type_room = input()
rate = input()

price = 0
days = days - 1
if type_room == "room for one person":
    price = 18 * days
elif type_room == "apartment":
    price = 25 * days
    if days < 10:
        price = price - (price * 0.3)
    elif 10 <= days <= 15:
        price = price - (price * 0.35)
    elif days > 15:
        price = price - (price * 0.5)
elif type_room == "president apartment":
    price = 35 * days
    if days < 10:
        price = price - (price * 0.1)
    elif 10 <= days <= 15:
        price = price - (price * 0.15)
    elif days > 15:
        price = price - (price * 0.2)

if rate == "positive":
    price = price + (price * 0.25)
else:
    price = price - (price * 0.1)

print(f"{price:.2f}")