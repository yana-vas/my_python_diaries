days = int(input())
hours = int(input())
total_money = 0
for d in range(1, days+1):
    current_money = 0
    for h in range(1, hours+1):
        if d % 2 == 0 and h % 2 != 0:
            current_money += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            current_money += 1.25
        else:
            current_money += 1.0
    total_money += current_money
    print(f"Day: {d} - {current_money:.2f} leva")
print(f"Total: {total_money:.2f} leva")
