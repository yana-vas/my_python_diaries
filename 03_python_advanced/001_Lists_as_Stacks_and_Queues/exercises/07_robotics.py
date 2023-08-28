from collections import deque


def coverts_str_to_seconds(str_time):
    hours, minutes, seconds = list(map(int, str_time.split(':')))
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_seconds_to_str_time(seconds):
    seconds %= 24 * 60 * 60

    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots_data = input().split(';')
process_time_by_robot = {}
busy_until_by_robot = {}

for robot_data in robots_data:
    name, process_time = robot_data.split('-')
    process_time_by_robot[name] = int(process_time)
    busy_until_by_robot[name] = -1

time = coverts_str_to_seconds(input())
items = deque()

command = input()
while command != 'End':
    items.append(command)
    command = input()

while items:
    time += 1
    item = items.popleft()

    for name, busy_until in busy_until_by_robot.items():
        if time >= busy_until:
            busy_until_by_robot[name] = time + process_time_by_robot[name]
            print(f"{name} - {item} [{convert_seconds_to_str_time(time)}]")
            break
    else:
        items.append(item)

# ROB-15;SS2-10;NX8000-3
# 24:59:00
# detail
# glass
# wood
# apple
# End
