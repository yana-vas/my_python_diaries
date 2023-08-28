from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
cars_counter = 0
crashed = False

command = input()
while command != 'END':
    if command == 'green':
        if cars:
            car = cars.popleft()
            seconds_left = green_light_duration - len(car)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    car = cars.popleft()
                    seconds_left -= len(car)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if free_window_duration >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                index = seconds_left + free_window_duration
                print('A crash happened!')
                print(f'{car} was hit at {car[index]}.')
                crashed = True
                break

    else:
        cars.append(command)

    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")