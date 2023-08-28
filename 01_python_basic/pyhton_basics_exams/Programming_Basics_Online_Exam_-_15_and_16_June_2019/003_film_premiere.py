projection = input()
packet_film = input()
tickets = int(input())

tickets_price = tickets
if projection == "John Wick":
    if packet_film == "Drink":
        tickets_price *= 12
    elif packet_film == "Popcorn":
        tickets_price *= 15
    elif packet_film == "Menu":
        tickets_price *= 19
elif projection == "Star Wars":
    if packet_film == "Drink":
        tickets_price *= 18
    elif packet_film == "Popcorn":
        tickets_price *= 25
    elif packet_film == "Menu":
        tickets_price *= 30
    if tickets >= 4:
        tickets_price -= 30*tickets_price/100
elif projection == "Jumanji":
    if packet_film == "Drink":
        tickets_price *= 9
    elif packet_film == "Popcorn":
        tickets_price *= 11
    elif packet_film == "Menu":
        tickets_price *= 14
    if tickets == 2:
        tickets_price -= 15*tickets_price/100
print(f"Your bill is {tickets_price:.2f} leva.")
