notes = ["0"] * 10
command = input().split('-')
while command[0] != 'End':
    priority = int(command[0]) - 1
    note = command[1]
    notes.pop(priority)
    notes.insert(priority, note)
    command = input().split('-')
filtered = [element for element in notes if element != "0"]
print(filtered)