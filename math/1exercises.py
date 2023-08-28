# първа задача

a = int(input())
b = int(input())
# b = 15
# a = 5
# 15 / 6 = 2.5
if (b % a) == 0: # 15 / 5 = 3.0
    print("a is divisor of b")
    print(f"a = {a}")
else:
    print("a is not divisor of b")
    print("Try again")
    while (b % a) != 0:
        a = int(input())
        b = int(input())
        if (b % a) == 0:
            print("a is divisor of b")
            print(f"a = {a}")
            break
        else:
            print("a is not divisor of b")
            print("Try again")




