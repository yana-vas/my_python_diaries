width = int(input())
length = int(input())
number_of_pieces = width * length

while number_of_pieces > 0:
    command_pieces = input()
    if command_pieces == "STOP":
        break
    else:
        command_pieces = int(command_pieces)
        number_of_pieces -= command_pieces
if number_of_pieces <= 0:
    needed_pieces = abs(number_of_pieces)
    print(f"No more cake left! You need {needed_pieces} pieces more.")
if command_pieces == "STOP":
    print(f"{number_of_pieces} pieces are left.")