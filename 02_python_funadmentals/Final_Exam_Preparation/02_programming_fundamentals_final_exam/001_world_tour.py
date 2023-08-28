stops = input()
command = input()
while command != "Travel":
    command = command.split(':')
    if command[0] == "Add Stop":
        index = int(command[1])
        if index in range(len(stops)):
            string = command[2]
            list_stops = list(stops)
            list_stops.insert(index, string)
            stops = ''.join(list_stops)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            list_stops = list(stops)
            stops = ''.join([stops[i] for i in range(len(stops)) if i < start_index or i > end_index])
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")