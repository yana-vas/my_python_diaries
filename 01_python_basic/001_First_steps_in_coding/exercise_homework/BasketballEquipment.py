anual_fee = int(input())

sneakers_price = anual_fee - (0.4*anual_fee)
outfit_price = sneakers_price - (0.2*sneakers_price)
ball = outfit_price/4
accessories = ball/5

sum = sneakers_price + outfit_price + ball + accessories + anual_fee
print(sum)