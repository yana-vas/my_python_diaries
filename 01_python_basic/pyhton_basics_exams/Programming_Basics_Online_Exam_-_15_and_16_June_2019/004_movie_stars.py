budget = float(input())
command = input()
reward = 0.0
while command != "ACTION":
    actor_name = command

    if len(actor_name) <= 15:
        reward = float(input())
    else:
        reward = 20 * budget / 100
    budget -= reward
    if budget <= 0:
        break
    command = input()
if budget > 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")
