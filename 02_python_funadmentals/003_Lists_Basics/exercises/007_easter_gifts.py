gifts = input().split(" ")
command = input()
while command != "No Money":
    index = 0
    list_command = command.split(" ")
    if list_command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if list_command[1] == gifts[i]:
                gifts[i] = "None"
    elif list_command[0] == "Required":
        index = int(list_command[2])
        if len(gifts) > index >= 0:
            gifts[index] = list_command[1]
    elif list_command[0] == "JustInCase":
        gifts[-1] = list_command[1]
    command = input()
for i in range(len(gifts)-1, -1, -1):
    if "None" == str(gifts[i]):
        gifts.remove(gifts[i])
print(" ".join(gifts))

