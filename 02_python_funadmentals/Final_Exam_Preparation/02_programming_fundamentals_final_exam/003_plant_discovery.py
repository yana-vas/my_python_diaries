def rate(plant_info, planets, planet):
    rating = float(plant_info[1])
    if planet in planets.keys():
        planets[planet]['rating'] += [rating]
    else:
        print('error')


def update(planet_info, planets, planet):
    new_rarity = planet_info[1]
    if planet in planets.keys():
        planets[planet]["rarity"] = new_rarity
    else:
        print('error')


n = int(input())

planets = {}
for i in range(n):
    planet_info = input().split('<->')
    planet = planet_info[0]
    rarity = planet_info[1]
    planets[planet] = {}
    planets[planet]["rarity"] = rarity
    planets[planet]["rating"] = []

command = input()
while command != "Exhibition":
    command = str(command).split(': ')
    command_name = command[0]
    planet_info = str(command[1]).split(' - ')
    planet = planet_info[0]
    if command_name == "Rate":
        rate(planet_info, planets, planet)
    elif command_name == "Update":
        update(planet_info, planets, planet)
    elif command_name == "Reset":
        if planet in planets.keys():
            planets[planet]['rating'] = []
        else:
            print('error')
    command = input()
print(f"Plants for the exhibition:")
for planet_name, planett_info in planets.items():
    rating = planets[planet_name]['rating']
    all_ratings = 0
    if rating == []:
        average_rating = 0.00
    else:
        for rate in rating:
            all_ratings += rate
        average_rating = all_ratings / len(rating)
    print(f"- {planet_name}; Rarity: {planets[planet_name]['rarity']}; Rating: {average_rating:.2f}")