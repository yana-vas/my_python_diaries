parentheses = list(input())
parentheses_data = {"{": "}", "(": ")", "[": "]"}
if len(parentheses) % 2 == 0:
    middle_index = len(parentheses) // 2
    first_half = parentheses[:middle_index]
    second_half = parentheses[middle_index:]
    failed = False
    for symbol in first_half:
        if symbol not in '({[':
            break
        if second_half.pop() != parentheses_data[symbol]:
            failed = True
            break
    if failed:
        print('NO')
    else:
        print('YES')
else:
    print('NO')
