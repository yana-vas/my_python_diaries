import re
password = input()
command = input()
while command != 'Complete':
    command = command.split(' ')
    if command[0] == 'Make':
        index = int(command[2])
        if command[1] == 'Upper':
            password = password[:index] + password[index].upper() + password[index+1:]
        elif command[1] == 'Lower':
            password = password[:index] + password[index].lower() + password[index + 1:]
        print(password)
    elif command[0] == 'Insert':
        index = int(command[1])
        char = command[2]
        if index in range(len(password)):
            password = list(password)
            password.insert(index, char)
            password = ''.join(password)
            print(password)
    elif command[0] == 'Replace':
        char = command[1]
        value = int(command[2])
        if char in password:
            new_char = chr(ord(char) + value)
            password = password.replace(char, new_char)
            print(password)
    elif command[0] == 'Validation':
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        if not all(x.isalpha() or x == '_' or x.isdigit() for x in password):
            print("Password must consist only of letters, digits and _!")
        if not re.search(r"[A-Z]+", password):
            print("Password must consist at least one uppercase letter!")
        if not re.search(r"[a-z]+", password):
            print("Password must consist at least one lowercase letter!")
        if not re.search(r"[0-9]+", password):
            print("Password must consist at least one digit!")
    command = input()