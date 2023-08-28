import string

number = int(input())
for i in range(number):
    for k in range(number):
        for j in range(number):
            print(f"{string.ascii_lowercase[i]}{string.ascii_lowercase[k]}{string.ascii_lowercase[j]}")
