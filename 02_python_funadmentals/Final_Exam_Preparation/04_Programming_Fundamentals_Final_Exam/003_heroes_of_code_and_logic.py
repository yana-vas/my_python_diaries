def cast_spell(command, heroes_info):
    hero_name = command[1]
    mp_needed = int(command[2])
    spell_name = command[3]
    if int(heroes_info[hero_name]["MP"]) >= mp_needed:
        heroes_info[hero_name]["MP"] -= mp_needed
        mana_points_left = int(heroes_info[hero_name]["MP"])
        print(f"{hero_name} has successfully cast {spell_name} and now has {mana_points_left} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(command, heroes_info):
    hero_name = command[1]
    damage = int(command[2])
    attacker = command[3]
    if int(heroes_info[hero_name]["HP"]) - damage > 0:
        heroes_info[hero_name]["HP"] -= damage
        current_hp = heroes_info[hero_name]["HP"]
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
    else:
        del heroes_info[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")


def recharge(command, heroes_infor):
    hero_name = command[1]
    amount = int(command[2])
    if heroes_info[hero_name]["MP"] + amount > 200:
        amount = amount - ((heroes_info[hero_name]["MP"] + amount) - 200)
        heroes_info[hero_name]["MP"] = 200
    else:
        heroes_info[hero_name]["MP"] += amount
    print(f"{hero_name} recharged for {amount} MP!")


def heal(command, heroes_info):
    hero_name = command[1]
    amount = int(command[2])
    if heroes_info[hero_name]["HP"] + amount > 100:
        amount = amount - ((heroes_info[hero_name]["HP"] + amount) - 100)
        heroes_info[hero_name]["HP"] = 100
    else:
        heroes_info[hero_name]["HP"] += amount
    print(f"{hero_name} healed for {amount} HP!")


n = int(input()) # the number of heroes that you can choose for your party

heroes_info = {}

for i in range(n):
    hero_info = input().split()

    hit_points = int(hero_info[1])
    mana_points = int(hero_info[2])

    heroes_info[hero_info[0]] = {}
    heroes_info[hero_info[0]]["HP"] = hit_points
    heroes_info[hero_info[0]]["MP"] = mana_points

command = input()
while command != 'End':
    command = command.split(" - ")
    if command[0] == 'CastSpell':
        cast_spell(command, heroes_info)
    elif command[0] == "TakeDamage":
        take_damage(command, heroes_info)
    elif command[0] == "Recharge":
        recharge(command, heroes_info)
    elif command[0] == "Heal":
        heal(command, heroes_info)
    command = input()

for name, info in heroes_info.items():
    print(name)
    hp = heroes_info[name]["HP"]
    mp = heroes_info[name]["MP"]
    print(f"  HP: {hp}")
    print(f"  MP: {mp}")