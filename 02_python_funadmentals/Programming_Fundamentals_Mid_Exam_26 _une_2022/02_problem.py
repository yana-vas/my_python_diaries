vehicles = input().split('>>')
total_tax_collected = 0
for car in vehicles:
    car_elements = car.split(' ')
    car_type = car_elements[0]
    years_to_be_paid = int(car_elements[1])
    kilometers = int(car_elements[2])
    initial_tax = 0
    additional_taxes = 0
    additional_promotions = 0
    if car_type == 'family':
        initial_tax = 50
        additional_promotions = years_to_be_paid*5
        additional_taxes = (kilometers // 3000) * 12
    elif car_type == 'heavyDuty':
        initial_tax = 80
        additional_promotions = years_to_be_paid * 8
        additional_taxes = (kilometers // 9000) * 14
    elif car_type == 'sports':
        initial_tax = 100
        additional_promotions = years_to_be_paid * 9
        additional_taxes = (kilometers // 2000) * 18
    else:
        print('Invalid car category.')
        continue
    tax_current_car = additional_taxes + (initial_tax - additional_promotions)
    total_tax_collected += tax_current_car
    print(f"A {car_type} car will pay {tax_current_car:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
