activation_key = input()
command = input()
while command != "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring not in activation_key:
            print("Substring not found!")
        else:
            print(f"{activation_key} contains {substring}")
        command = input()
        continue
    elif command[0] == "Flip":
        upper_or_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        wanted_substring = activation_key[start_index:end_index]
        if upper_or_lower == 'Upper':
            wanted_substring = wanted_substring.upper()
        elif upper_or_lower == "Lower":
            wanted_substring = wanted_substring.lower()
        activation_key = activation_key[:start_index] + wanted_substring + activation_key[end_index:]
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        wanted_substring = activation_key[start_index:end_index]
        activation_key = activation_key.replace(wanted_substring, '')
    print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")