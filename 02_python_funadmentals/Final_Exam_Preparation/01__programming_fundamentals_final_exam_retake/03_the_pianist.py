def add(cmd):
    piece = cmd[1]
    composer = cmd[2]
    key = cmd[3]
    if piece in pieces_info.keys():
        return (f"{piece} is already in the collection!")
    else:
        pieces_info[piece] = {}
        pieces_info[piece]["composer"] = composer
        pieces_info[piece]["key"] = key
        return (f"{piece} by {composer} in {key} added to the collection!")


def remove(cmd):
    piece = cmd[1]
    if piece in pieces_info.keys():
        del pieces_info[piece]
        return f"Successfully removed {piece}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."


def change_key(cmd):
    piece = cmd[1]
    new_key = cmd[2]
    if piece in pieces_info.keys():
        pieces_info[piece]['key'] = new_key
        return f"Changed the key of {piece} to {new_key}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."

n = int(input())

pieces_info = {}
for i in range(n):
    info = input().split('|')
    piece = info[0]
    composer = info[1]
    key = info[2]
    pieces_info[piece] = {}
    pieces_info[piece]["composer"] = composer
    pieces_info[piece]["key"] = key

command = input()
while command != "Stop":
    command = command.split('|')
    if command[0] == "Add":
        print(add(command))
    elif command[0] == "Remove":
        print(remove(command))
    elif command[0] == "ChangeKey":
        print(change_key(command))
    command = input()

for curr_piece, value in pieces_info.items():
    curr_composer = pieces_info[curr_piece]["composer"]
    curr_key = pieces_info[curr_piece]["key"]
    print(f"{curr_piece} -> Composer: {curr_composer}, Key: {curr_key}")