count_steps = 0

while count_steps < 10000:
    command = input()

    if command == "Going home":
        steps_to_home = int(input())
        count_steps += steps_to_home
        break
    else:
        walked_steps = int(command)
        count_steps += walked_steps

if count_steps >= 10000:
    steps_over_the_goal = count_steps - 10000
    print('Goal reached! Good job!')
    print(f'{abs(steps_over_the_goal)} steps over the goal!')
else:
    print(f'{10000 - count_steps} more steps to reach goal.')