heroes = {}
command = input()
while command != 'End':
    command = command.split(' ')
    hero_name = command[1]
    if command[0] == "Enroll":
        if hero_name not in heroes.keys():
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif command[0] == "Learn":
        spell_name = command[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)
    elif command[0] == 'Unlearn':
        spell_name = command[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)
    command = input()
print("Heroes:")
for name, spell_book in heroes.items():
    print(f"== {name}: {', '.join(spell_book)}")