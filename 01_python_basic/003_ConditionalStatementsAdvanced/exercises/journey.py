budget = float(input())
season = input()

vacation_type = ""
destination = ""
price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_type = "Camp"
        price = budget * 0.3
    elif season == "winter":
        vacation_type = "Hotel"
        price = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_type = "Camp"
        price = budget * 0.4
    elif season == "winter":
        vacation_type = "Hotel"
        price = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    vacation_type = "Hotel"
    price = budget * 0.9

# "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
# "{Вид почивка} - {Похарчена сума}"
print(f"Somewhere in {destination}")
print(f"{vacation_type} - {price:.2f}")