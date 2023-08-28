month = input()
number_of_nights = int(input())

price_for_studio = 0
price_for_apartment = 0

if month == "May" or month == "October":
    price_for_studio = 50 * number_of_nights
    price_for_apartment = 65 * number_of_nights
    if 14 >= number_of_nights > 7:
        price_for_studio = price_for_studio - (price_for_studio * 0.05)
    elif number_of_nights > 14:
        price_for_studio = price_for_studio - (price_for_studio * 0.3)
elif month == "June" or month == "September":
    price_for_studio = 75.20 * number_of_nights
    price_for_apartment = 68.70 * number_of_nights
    if number_of_nights > 14:
        price_for_studio = price_for_studio - (price_for_studio * 0.2)
elif month == "August" or month == "July":
    price_for_studio = 76 * number_of_nights
    price_for_apartment = 77 * number_of_nights

if number_of_nights > 14:
    price_for_apartment = price_for_apartment - (price_for_apartment * 0.1)

print(f"Apartment: {price_for_apartment:.2f} lv.")
print(f"Studio: {price_for_studio:.2f} lv.")