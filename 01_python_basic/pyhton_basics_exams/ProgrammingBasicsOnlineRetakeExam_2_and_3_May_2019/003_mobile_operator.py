duration_of_contract = input() # one/two
type_of_the_contract = input() #small, middle, large, extralarge
mobile_internet = input() #yes / no
months = int(input()) # [1...24]

price = 0
if duration_of_contract == "one":
    if type_of_the_contract == "Small":
        price = 9.98 * months
    elif type_of_the_contract == "Middle":
        price = 18.99 * months
    elif type_of_the_contract == "Large":
        price = 25.98 * months
    elif type_of_the_contract == "ExtraLarge":
        price = 35.99 * months
elif duration_of_contract == "two":
    if type_of_the_contract == "Small":
        price = 8.58 * months
    elif type_of_the_contract == "Middle":
        price = 17.09 * months
    elif type_of_the_contract == "Large":
        price = 23.59 * months
    elif type_of_the_contract == "ExtraLarge":
        price = 31.79 * months
if mobile_internet == "yes":
    if type_of_the_contract == "Small":
        price += 5.50 * months
    elif type_of_the_contract == "Large" or type_of_the_contract == "Middle":
        price += 4.35 * months
    elif type_of_the_contract == "ExtraLarge":
        price += 3.85 * months
if duration_of_contract == "two":
    price -= (3.75 * price)/100
print(f"{price:.2f} lv.")
