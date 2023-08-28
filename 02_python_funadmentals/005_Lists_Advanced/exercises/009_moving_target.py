targets_value = list(map(int, input().split(' ')))
command = input()
while command != 'End':
    command = command.split(' ')
    index = int(command[1])
    if command[0] == 'Shoot':
        power = int(command[2])
        if index in range(len(targets_value)):
            if targets_value[index] - power > 0:
                targets_value[index] -= power
            else:
                targets_value.pop(index)
    elif command[0] == 'Add':
        value = int(command[2])
        if index in range(len(targets_value)):
            targets_value.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == 'Strike':
        radius = int(command[2])
        before_radius = index - radius
        after_radius = index + radius
        if after_radius in range(len(targets_value)) and before_radius in range(len(targets_value)):
            targets_value = targets_value[0:before_radius] + targets_value[after_radius + 1::]
        else:
            print("Strike missed!")
    command = input()
targets_value = list(map(str, targets_value))
print('|'.join(targets_value))
