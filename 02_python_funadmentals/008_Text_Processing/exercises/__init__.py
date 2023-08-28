my_ticket = input()
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
    print(f"ticket \"{my_ticket}\" - {len(first_halve)}{first_halve[0]}")
