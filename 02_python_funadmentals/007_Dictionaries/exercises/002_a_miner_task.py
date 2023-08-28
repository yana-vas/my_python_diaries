command = input()
line_counter = 0
minor = {}
resources = []
values = []
while command != 'stop':
    line_counter += 1
    if line_counter % 2 == 0:
        if resource in minor:
            minor[resource] += int(command)
        else:
            minor[resource] = int(command)
    else:
        resource = command
    command = input()
for key, value in minor.items():
    print(f"{key} -> {value}")
