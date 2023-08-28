football_team = input()
number_of_tournaments = int(input())
win_counter = 0
equal_counter = 0
loose_counter = 0
points_sum = 0
for i in range(number_of_tournaments):
    result = input()
    if result == 'W':
        win_counter += 1
        points_sum += 3
    elif result == 'D':
        equal_counter += 1
        points_sum += 1
    elif result == 'L':
        loose_counter +=1
if number_of_tournaments == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    print(f"{football_team} has won {points_sum} points during this season.")
    print("Total stats:")
    print(f"## W: {win_counter}")
    print(f"## D: {equal_counter}")
    print(f"## L: {loose_counter}")
    print(f"Win rate: {win_counter/number_of_tournaments*100:.2f}%")
