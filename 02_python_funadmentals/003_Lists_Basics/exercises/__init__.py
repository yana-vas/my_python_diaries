coins = [int(num) for num in input().split(", ")]
beggars = int(input())
index = 0
beggars_list = [0] * beggars
for coin in coins:
    beggars_list[index] += coin
    index += 1
    if index >= beggars:
        index = 0
print(beggars_list)
