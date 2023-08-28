command = input()
force_book = {}
while command != "Lumpawaroo":
    users_in_force_book = [' '.join(v) for k, v in force_book.items()]
    users_in_force_book = ' '.join(users_in_force_book)
    if " | " in command:
        command = command.split(' | ')
        force_side = command[0]
        force_user = command[1]
        if force_user not in users_in_force_book and force_side not in force_book.keys():
            force_book[force_side] = []
            force_book[force_side].append(force_user)
        elif force_user not in users_in_force_book:
            force_book[force_side].append(force_user)
        elif force_user in users_in_force_book:
            continue
    elif ' -> ' in command:
        command = command.split(' -> ')
        force_side = command[1]
        force_user = command[0]
        for total_sides in force_book.keys():
            if force_user in force_book[total_sides]:
                force_book[total_sides].remove(force_user)
        if force_user not in users_in_force_book and force_side not in force_book.keys():
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for force_side, force_users in force_book.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for user in force_users:
            print(f"! {user}")

