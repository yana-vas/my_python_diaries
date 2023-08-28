number = input()


def odd_and_even_sum(num):
    even = []
    odd = []
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            even.append(int(num[i]))
        else:
            odd.append(int(num[i]))
    return print(f"Odd sum = {sum(odd)}, Even sum = {sum(even)}")


odd_and_even_sum(num=number)

