from collections import deque

n = int(input())  # petrol pumps
pumps = deque()

for i in range(n):
    pumps_data = list(map(int, input().split(' ')))
    pumps.append(pumps_data)

for attempt in range(n):
    tank = 0
    failed = False
    for fuel, distance in pumps:
        tank += fuel

        if distance > tank:
            failed = True
            break
        else:
            tank -= distance

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
