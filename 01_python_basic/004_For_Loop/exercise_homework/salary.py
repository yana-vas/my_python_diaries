number_of_websites = int(input())
salary = int(input())

money_lost = 0
for i in range(number_of_websites):
    current_website = input()
    if current_website == "Facebook":
        money_lost += 150
    elif current_website == "Instagram":
        money_lost += 100
    elif current_website == "Reddit":
        money_lost += 50
    if money_lost >= salary:
        break

salary_left = abs(money_lost - salary)
if money_lost >= salary:
    print("You have lost your salary.")
else:
    print(f"{salary_left}")
