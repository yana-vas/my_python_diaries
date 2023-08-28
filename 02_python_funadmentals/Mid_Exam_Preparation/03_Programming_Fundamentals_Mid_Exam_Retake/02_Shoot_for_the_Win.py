targets = [int(num) for num in input().split(' ')]
command = input()
shot_targets = 0


def changed(a_list, value):
    for i in range(len(a_list)):
        num = a_list[i]
        if num != -1 and num > value:
            a_list[i] = num - value
        elif num != -1 and num <= value:
            a_list[i] = num + value


while command != 'End':
    index = int(command)
    if index > len(targets) - 1 or index < 0:
        command = input()
        continue
    current_value = targets[index]
    if targets[index] != -1:
        targets[index] = -1
        shot_targets += 1
        changed(targets, current_value)
    command = input()
targets = list(map(str, targets))
print(f"Shot targets: {shot_targets} -> {' '.join(targets)}")
