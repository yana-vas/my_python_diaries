def move(cmd, message):
    n = int(cmd[1])  # number of letters
    message = ''.join(
        [message[i] for i in range(len(message)) if i > n - 1] +
        [message[i] for i in range(len(message)) if i < n])
    return message


def insert(cmd, message):
    index = int(cmd[1])
    value = cmd[2]
    message = list(message)
    message.insert(index, value)
    return ''.join(message)


def change_all(cmd, message):
    substring = cmd[1]
    replacement = cmd[2]
    message = message.replace(substring, replacement)
    return message


encrypted_message = input()
command = input()
while command != "Decode":
    command = command.split("|")
    command_name = command[0]
    if command_name == "Move":
        encrypted_message = move(command, encrypted_message)
    elif command_name == "Insert":
        encrypted_message = insert(command, encrypted_message)
    elif command_name == "ChangeAll":
        encrypted_message = change_all(command, encrypted_message)
    command = input()
print(f"The decrypted message is: {encrypted_message}")