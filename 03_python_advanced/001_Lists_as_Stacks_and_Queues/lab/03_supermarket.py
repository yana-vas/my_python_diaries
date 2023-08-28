from collections import deque

people_deque = deque()

command = input()
while command != 'End':
    if command == 'Paid':
        while people_deque:
            print(people_deque.popleft())
    else:
        people_deque.append(command)
    command = input()
print(f"{len(people_deque)} people remaining.")