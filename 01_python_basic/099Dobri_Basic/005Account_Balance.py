word = input()

balance = 0
while word != "NoMoreMoney":
    sum_cur = float(input())
    if sum_cur > 0:
        print("Invalid operation!")
    print(f"Increase: {sum_cur}")
    balance += sum_cur
    word = input()
print(f"Total: {balance}")

