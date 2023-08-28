tickets = input().split(', ')


def is_valid(my_ticket):
    if len(my_ticket) == 20:
        return True
    else:
        return False


def is_winning(my_ticket):
    first_halve = ''
    second_halve = ''
    special_symbol = ''
    for i in range(len(my_ticket) // 2):
        char = my_ticket[i]
        if char == '@' or char == '#' or char == '$' or char == '^' and first_halve == '':
            special_symbol = char
        if char == special_symbol:
            first_halve += char
        else:
            if len(first_halve) < 6:
                first_halve = ''
            else:
                break

    for i in range(len(my_ticket) // 2, len(my_ticket)):
        char = my_ticket[i]

        if char == special_symbol:
            second_halve += char
        else:
            if len(second_halve) < 6:
                second_halve = ''
            else:
                break
    if len(first_halve) >= 6 and len(second_halve) >= 6:
        if len(first_halve) > len(second_halve):
            return second_halve
        else:
            return first_halve
    else:
        return 'False'


def jackpot(my_ticket):
    if my_ticket[0]*20 == my_ticket:
        if my_ticket[0] == '@' or my_ticket[0] == '#' or my_ticket[0] == '$' or my_ticket[0] == '^':
            return True
    else:
        return False


for ticket in tickets:
    ticket = ticket.strip()
    if not is_valid(ticket):
       print("invalid ticket")
    elif is_valid(ticket) and is_winning(ticket) == "False":
        print(f"ticket \"{ticket}\" - no match")
    elif is_valid(ticket) and is_winning(ticket) != 'False' and not jackpot(ticket):
        print(f"ticket \"{ticket}\" - {len(is_winning(ticket))}{is_winning(ticket)[0]}")
    elif jackpot(ticket):
        print(f"ticket \"{ticket}\" - {len(ticket)//2}{ticket[0]} Jackpot!")