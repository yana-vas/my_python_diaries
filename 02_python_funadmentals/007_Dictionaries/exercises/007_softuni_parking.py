num_of_commands = int(input())
fancy_parking = {}
for i in range(num_of_commands):
    command = input().split()
    username = command[1]
    if command[0] == 'register':
        if username in fancy_parking:
            print(f"ERROR: already registered with plate number {fancy_parking[username]}")
            continue
        license_plate_number = command[2]
        fancy_parking[username] = license_plate_number
        print(f"{username} registered {license_plate_number} successfully")
    else:
        if username not in fancy_parking:
            print(f"ERROR: user {username} not found")
            continue
        fancy_parking.pop(username)
        print(f"{username} unregistered successfully")

for username, license_plate_number in fancy_parking.items():
    print(f"{username} => {license_plate_number}")
