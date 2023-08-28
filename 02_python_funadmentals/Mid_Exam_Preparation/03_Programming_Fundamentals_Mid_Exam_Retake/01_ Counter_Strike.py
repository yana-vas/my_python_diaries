initial_energy = int(input())
command = input()
won_battles = 0
while command != 'End of battle':
    current_energy = int(command)
    if initial_energy < current_energy:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break
    initial_energy -= current_energy
    won_battles += 1
    if won_battles % 3 == 0:
        initial_energy += won_battles
    command = input()
if command == 'End of battle':
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}" )

