input_data = input().split(' ')
my_dict = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = ''
obtained = False
while True:
    materials = [material.lower() for material in input_data if material.isalpha()]
    quantities = [int(quantity) for quantity in input_data if quantity.isdigit()]
    for i in range(len(materials)):
        curr_material = materials[i]
        curr_quantity = quantities[i]
        if curr_material not in my_dict:
            my_dict[curr_material] = curr_quantity
        else:
            my_dict[curr_material] += curr_quantity
        if my_dict['shards'] >= 250:
            print("Shadowmourne obtained!")
            my_dict['shards'] -= 250
            obtained = True
        elif my_dict['fragments'] >= 250:
            print("Valanyr obtained!")
            my_dict['fragments'] -= 250
            obtained = True
        elif my_dict['motes'] >= 250:
            print("Dragonwrath obtained!")
            my_dict['motes'] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    input_data = input().split(' ')

for material, quantity in my_dict.items():
    print(f"{material}: {quantity}")