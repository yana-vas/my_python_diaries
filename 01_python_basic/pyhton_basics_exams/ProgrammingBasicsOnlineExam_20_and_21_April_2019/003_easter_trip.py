destination = input()
reservation_dates = input()
nights_booked = int(input())

price_for_a_night = 0
if destination == "France":
    if reservation_dates == "21-23":
        price_for_a_night = 30
    elif reservation_dates == "24-27":
        price_for_a_night = 35
    elif reservation_dates == "28-31":
        price_for_a_night = 40
elif destination == "Italy":
    if reservation_dates == "21-23":
        price_for_a_night = 28
    elif reservation_dates == "24-27":
        price_for_a_night = 32
    elif reservation_dates == "28-31":
        price_for_a_night = 39
elif destination == "Germany":
    if reservation_dates == "21-23":
        price_for_a_night = 32
    elif reservation_dates == "24-27":
        price_for_a_night = 37
    elif reservation_dates == "28-31":
        price_for_a_night = 43
price_for_all = price_for_a_night * nights_booked

print(f"Easter trip to {destination} : {price_for_all:.2f} leva.")