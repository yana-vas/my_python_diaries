number_of_sold_games = int(input())

hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0

for i in range(number_of_sold_games):
    game = input()
    if game == "Hearthstone":
        hearthstone_counter += 1
    elif game == "Fornite":
        fornite_counter += 1
    elif game == "Overwatch":
        overwatch_counter += 1
    else:
        others_counter += 1
print(f"Hearthstone - {hearthstone_counter/number_of_sold_games*100:.2f}%")
print(f"Fornite - {fornite_counter/number_of_sold_games*100:.2f}%")
print(f"Overwatch - {overwatch_counter/number_of_sold_games*100:.2f}%")
print(f"Others - {others_counter/number_of_sold_games*100:.2f}%")
