receipt = 0
while True:
    command = input()
    if command == 'special' or command == 'regular':
        break
    price = float(command)
    if price < 0:
        print('Invalid price!')
        continue
    receipt += price
if receipt == 0:
    print("Invalid order!")
else:
    taxes = receipt * 0.2
    total_price = receipt + taxes
    if command == 'special':
        total_price -= total_price * 0.1
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {receipt:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {total_price:.2f}$")
