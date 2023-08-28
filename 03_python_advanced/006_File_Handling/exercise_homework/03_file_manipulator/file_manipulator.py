import os.path

command = input()
while command != 'End':
    command = command.split('-')
    file_name = command[1]

    if command[0] == 'Create':
        open(file_name, 'w').close()
    elif command[0] == 'Add':
        content = command[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')
    elif command[0] == 'Replace':
        old_string = command[2]
        new_string = command[3]

        if not os.path.exists(file_name):
            print("An error occurred")
            command = input()
            continue

        with open(file_name, 'r+') as file:
            new_file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(new_file_content)

    elif command[0] == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    command = input()