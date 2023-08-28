a1 = int(input())
a2 = int(input())
n = int(input())

operation = int(n / 2 - 1)

for simbol_1 in range(a1, a2):
    if simbol_1 % 2 == 0:
        continue
    for simbol_2 in range(1, n):
        if operation == 1:
            if (simbol_2 + 1 + simbol_1) % 2 != 0:
                print(f"{chr(simbol_1)}-{simbol_2}{1}{simbol_1}")
            continue
        for simbol_3 in range(1, operation+1):
            if (simbol_2 + simbol_3 + simbol_1) % 2 != 0:
                print(f"{chr(simbol_1)}-{simbol_2}{simbol_3}{simbol_1}")

        

