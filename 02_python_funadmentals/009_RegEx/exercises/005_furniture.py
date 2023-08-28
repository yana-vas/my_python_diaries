import re
input_data = input()
bought_furniture = []
total_money = 0
pattern = r">>(?P<furniture>[a-zA-z]+)<<(?P<price>\d+\.*\d+)!(?P<quantity>\d+)"
while input_data != "Purchase":
    match = re.findall(pattern, input_data)
    if len(match) > 0:
        bought_furniture.append(match[0][0])
        total_money += float(match[0][1]) * int(match[0][2])
    input_data = input()
print("Bought furniture:")
[print(furniture) for furniture in bought_furniture]
print(f"Total money spend: {total_money:.2f}")
