command = input()
max_points = 0
powerful_film = ""
film_counter = 0
while command != "STOP":
    current_points = 0
    film = command
    film_counter += 1
    for character in film:

        current_points += ord(character)
        if character.islower():
            current_points -= 2 * len(film)
        elif character.isupper():
            current_points -= len(film)
    if current_points > max_points:
        max_points = current_points
        powerful_film = film

    if film_counter >= 7:
        break
    command = input()
if film_counter == 7:
    print(f"The limit is reached.")
print(f"The best movie for you is {powerful_film} with {max_points} ASCII sum.")