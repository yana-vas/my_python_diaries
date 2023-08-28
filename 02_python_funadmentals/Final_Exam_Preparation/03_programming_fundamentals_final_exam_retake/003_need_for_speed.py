n = int(input())

cars = {}
for i in range(n):
    car_info = input().split("|")
    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    cars[car] = {}
    cars[car]["mileage"] = mileage
    cars[car]["fuel"] = fuel


command = input()
while command != "Stop":
    command = command.split(' : ')
    car = command[1]
    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > cars[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        fuel = int(command[2])
        if fuel+cars[car]['fuel'] > 75:
            fuel = fuel - (fuel + cars[car]['fuel'] - 75)
        cars[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif command[0] == "Revert":
        kilometers = int(command[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
            command = input()
            continue
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()
for car in cars:
    car_mileage = cars[car]["mileage"]
    car_fuel = cars[car]["fuel"]
    print(f"{car} -> Mileage: {car_mileage} kms, Fuel in the tank: {car_fuel} lt.")
