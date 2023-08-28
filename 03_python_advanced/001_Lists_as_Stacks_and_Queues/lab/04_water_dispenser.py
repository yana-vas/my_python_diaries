from collections import deque

water_quantity = int(input())

people_deque = deque()
command = input()
while command != 'Start':
    people_deque.append(command)
    command = input()

command = input()
while command != 'End':
    if command.isdigit():
        if int(command) <= water_quantity:
            water_quantity -= int(command)
            print(f"{people_deque.popleft()} got water")
        else:
            print(f"{people_deque.popleft()} must wait")
    else:
        _, litters = command.split(' ')
        water_quantity += int(litters)
    command = input()
print(f"{water_quantity} liters left")