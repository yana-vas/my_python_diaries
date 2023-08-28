    # inpt = input()
# balance = 0.0
# while input != "NoMoreMoney":
#     amount = float(inpt)
#     if amount < 0:
#         print("Invalid operation!")
#         break
#     balance += amount
#     print(f"Increase: {amount:.2f}")
#     inpt = input()
# print(f"Total: {balance:.2f}")
input_line = input()

balance = 0
while input_line != "NoMoreMoney":
    amount = float(input_line)
    if amount < 0:
        print("Invalid operation!")
        break

    balance = balance + amount
    print(f"Increase: {amount:.2f}")

    input_line = input()

print(f"Total: {balance:.2f}")