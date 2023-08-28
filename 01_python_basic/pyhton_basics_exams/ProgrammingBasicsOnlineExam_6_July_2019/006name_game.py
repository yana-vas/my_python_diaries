import unicodedata

command = input()
winner_points = 0
looser_points = 0
winner_name = ""
while command != "Stop":
    points_counter = 0
    name = command
    for i in range(len(name)):
        number = int(input())
        if number == ord(name[i]):
            points_counter += 10
        else:
            points_counter += 2
    if points_counter >= winner_points:
        winner_points = points_counter
        winner_name = name
    command = input()
print(f"The winner is {winner_name} with {winner_points} points!")
