guests = int(input())
menu_tax_for_a_single_person = float(input())
budget = float(input())
cake_price = 0

if 10 <= guests <= 15:
    menu_tax_for_a_single_person -= menu_tax_for_a_single_person * 15/100
elif 15 < guests <= 20:
    menu_tax_for_a_single_person -= menu_tax_for_a_single_person * 20/100
elif guests > 20:
    menu_tax_for_a_single_person -= menu_tax_for_a_single_person * 25/100
cake_price = 10*budget/100

sum_for_the_party = cake_price + menu_tax_for_a_single_person * guests

if sum_for_the_party <= budget:
    money_left = budget - sum_for_the_party
    print(f"It is party time! {money_left:.2f} leva left.")
else:
    needed_money = sum_for_the_party - budget
    print(f"No party! {needed_money:.2f} leva needed.")