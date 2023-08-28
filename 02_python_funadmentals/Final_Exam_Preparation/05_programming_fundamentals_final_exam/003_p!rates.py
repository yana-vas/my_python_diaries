command = input()
cities_info = {}
while command != 'Sail':
    city_info = command.split('||')
    city = city_info[0]
    population = int(city_info[1])
    gold = int(city_info[2])
    if city not in cities_info.keys():
        cities_info[city] = {}
        cities_info[city]["population"] = population
        cities_info[city]["gold"] = gold
    else:
        cities_info[city]["population"] += population
        cities_info[city]["gold"] += gold
    command = input()

event_command = input()
while event_command != 'End':
    event_command = event_command.split('=>')
    town = event_command[1]
    if event_command[0] == 'Plunder':
        people = int(event_command[2])
        gold = int(event_command[3])
        cities_info[town]["population"] -= people
        cities_info[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_info[town]["population"] == 0 or cities_info[town]["gold"] == 0:
            del cities_info[town]
            print(f"{town} has been wiped off the map!")
    elif event_command[0] == 'Prosper':
        gold = int(event_command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_info[town]["gold"] += gold
            total_gold = cities_info[town]["gold"]
            print(f"{gold} gold added to the city treasury. {town} now has {total_gold} gold.")
    event_command = input()
if len(cities_info) > 0:
    print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
    for city in cities_info:
        city_population = cities_info[city]["population"]
        city_gold = cities_info[city]["gold"]
        print(f"{city} -> Population: {city_population} citizens, Gold: {city_gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")