wagons = int(input())
train = [0 for x in range(wagons)]


def train_operations(train_list, key_word, value):
    if key_word == 'add':
        train_list[-1] = int(train_list[-1]) + int(value[1])
    elif key_word == "insert":
        train_list[int(value[1])] = int(train_list[int(value[1])]) + int(value[2])
    elif key_word == 'leave':
        train_list[int(value[1])] = int(train_list[int(value[1])]) - int(value[2])
    return train


command = input().split(' ')
while command[0] != 'End':
    train_operations(train_list=train, key_word=command[0], value=command)
    command = input().split(' ')
print(train)
