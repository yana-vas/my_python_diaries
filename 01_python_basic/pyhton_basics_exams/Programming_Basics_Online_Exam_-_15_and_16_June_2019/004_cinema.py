capacity = int(input())
command = input()
free_seats = capacity
counter_seats = 0
the_sum = 0
while command != "Movie time!":
    people_entering_in_the_cinema = int(command)
    counter_seats += people_entering_in_the_cinema
    free_seats -= people_entering_in_the_cinema
    if free_seats < 0:
        break
    the_sum += 5 * people_entering_in_the_cinema
    if people_entering_in_the_cinema*1.0 % 3 == 0:
        the_sum -= 5
    command = input()
if command == "Movie time!":
    print(f"There are {free_seats} seats left in the cinema.")
else:
    print("The cinema is full.")
print(f"Cinema income - {the_sum} lv.")
