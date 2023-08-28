age = int(input())
price_for_washing_machine = float(input())
price_for_a_single_toy = int(input())

toys = 0
money = 0
birthday_money = 0
for birthday in range(1, age+1):
    if birthday % 2 == 0:
        birthday_money += 10
        money += birthday_money - 1
    else:
        toys += 1
money += toys * price_for_a_single_toy

if money >= price_for_washing_machine:
    remaining_money = money - price_for_washing_machine
    print(f"Yes! {remaining_money:.2f}")
else:
    needed_money = abs(price_for_washing_machine - money)
    print(f"No! {needed_money:.2f}")
