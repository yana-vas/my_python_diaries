products_list = input().split(' ')
products = {}
wanted_products = input().split(' ')
for i in range(0, len(products_list), 2):
    key = products_list[i]
    value = products_list[i + 1]
    products[key] = int(value)
for curr_product in wanted_products:
    if curr_product in products:
        print(f"We have {products[curr_product]} of {curr_product} left")
    else:
        print(f"Sorry, we don't have {curr_product}")
