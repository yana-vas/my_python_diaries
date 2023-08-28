import re

pattern = r"(@#+([A-Z]([a-zA-Z0-9]){4,}[A-Z])@#+)"

n = int(input())
for i in range(n):
    product_group = ''
    barcode = input()
    match = re.findall(pattern, barcode)
    is_digit_in_barcode = False
    if len(match) > 0:
        for char in match[0][1]:
            if str(char).isdigit():
                is_digit_in_barcode = True
                product_group += char
        if not is_digit_in_barcode:
            product_group = '00'
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
