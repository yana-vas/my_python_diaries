city = input()
type_packet = input()
VIP = input()
number_of_overnights_stay = int(input())
price = 0
if number_of_overnights_stay > 7:
    number_of_overnights_stay -= 1
elif number_of_overnights_stay < 1:
    print("Days must be positive number!")
    exit()
if city == "Bansko" or city == "Borovets":

    if type_packet == "withEquipment":
        price = 100 * number_of_overnights_stay
        if VIP == "yes":
            price -= 10 * price / 100
    elif type_packet == "noEquipment":
        price = 80 * number_of_overnights_stay
        if VIP == "yes":
            price -= 5 * price / 100
    else:
        print("Invalid input!")
        exit()
elif city == "Varna" or city == "Burgas":
    if type_packet == "withBreakfast":
        price = 130 * number_of_overnights_stay
        if VIP == "yes":
            price -= 12 * price / 100
    elif type_packet == "noBreakfast":
        price = 100 * number_of_overnights_stay
        if VIP == "yes":
            price -= 7 * price / 100
    else:
        print("Invalid input!")
        exit()
else:
    print("Invalid input!")
    exit()

print(f"The price is {price:.2f}lv! Have a nice time!")
