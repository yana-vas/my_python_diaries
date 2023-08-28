events = input().split("|")
energy = 100    # initial_energy = 100
coins = 100     # initial_coins = 100
finished_all_events = True
for index in range(len(events)):
    current_event = events[index].split("-")
    event_or_ingredient = current_event[0]
    number = int(current_event[1])
    if event_or_ingredient == "rest":
        gained_energy = 0
        if number + energy <= 100:
            energy += number
            gained_energy = number
        else:
            if energy == 100:
                gained_energy = 0
            else:
                additional_energy = energy + number - 100
                gained_energy = number - additional_energy
                energy = energy + number - additional_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_or_ingredient == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            finished_all_events = False
            break
if finished_all_events:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
