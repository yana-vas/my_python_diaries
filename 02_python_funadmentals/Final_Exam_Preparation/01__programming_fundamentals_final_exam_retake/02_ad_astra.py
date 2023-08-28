import re
text = input()

pattern = r"(?P<char>[?<=#|\|])([a-zA-Z\s]+)(?P=char)(\d{2}/\d{2}/\d{2})(?P=char)(\d{0,10000})(?P=char)"

total_calories = 0
match = re.findall(pattern, text)
for product_info in match:
    calories = int(product_info[3])
    total_calories += calories
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for el in match:
    print(f"Item: {el[1]}, Best before: {el[2]}, Nutrition: {el[3]}")