team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sequence_of_cards = input()
list_of_sequence_of_cards = sequence_of_cards.split(" ")
for element in list_of_sequence_of_cards:
    current_card = element.split("-")
    current_team = current_card[0]
    current_player = int(current_card[1])

    if 'A' == current_team:
        if current_player not in team_A:
            continue
        team_A.remove(current_player)
    else:
        if current_player not in team_B:
            continue
        team_B.remove(current_player)
    if len(team_A) < 7 or len(team_B) < 7:
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if len(team_A) < 7 or len(team_B) < 7:
    print("Game was terminated")


