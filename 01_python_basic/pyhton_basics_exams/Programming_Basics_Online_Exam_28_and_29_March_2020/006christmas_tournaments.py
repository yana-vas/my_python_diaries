days_tournaments = int(input())
money_counter = 0
win_counter = 0
lose_counter = 0

for i in range(days_tournaments):
    money_for_the_day = 0
    current_win_counter = 0
    current_lose_counter = 0
    command = input()
    while command != "Finish":
        current_money = 0
        sport = command
        result = input()
        if result == "win":
            current_money += 20
            money_for_the_day += 20
            current_win_counter += 1
            win_counter += 1

        else:
            current_lose_counter += 1
            lose_counter += 1
        command = input()

    if current_win_counter > current_lose_counter:
        money_for_the_day += money_for_the_day * 0.1
        money_counter += money_for_the_day
    else:
        money_counter += money_for_the_day

if win_counter > lose_counter:
    money_counter += money_counter * 0.2
    print(f"You won the tournament! Total raised money: {money_counter:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_counter:.2f}")
