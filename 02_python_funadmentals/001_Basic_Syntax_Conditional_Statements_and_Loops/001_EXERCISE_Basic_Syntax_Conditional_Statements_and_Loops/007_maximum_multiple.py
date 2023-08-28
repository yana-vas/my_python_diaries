divisor = int(input())
bond = int(input())


for n in range(bond, 1, -1):
    if n % divisor == 0:
        if n > 0:
            print(n)
            break
