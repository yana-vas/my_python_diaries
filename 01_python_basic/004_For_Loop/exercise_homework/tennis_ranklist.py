import math

number_of_tournaments = int(input())
rankings_points = int(input())

total_points = rankings_points
number_of_won = 0
for i in range(number_of_tournaments):
    reached_stage = input()
    if reached_stage == "W":
        total_points += 2000
        number_of_won += 1
    elif reached_stage == "F":
        total_points += 1200
    elif reached_stage == "SF":
        total_points += 720
average_points = (total_points - rankings_points)/number_of_tournaments
percentage_of_tournaments_won = (number_of_won / number_of_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage_of_tournaments_won:.2f}%")
