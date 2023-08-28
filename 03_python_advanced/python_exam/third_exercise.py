
def forecast(*args):
    my_list = []
    sunny = []
    rainy = []
    cloudy = []
    for key in args:
        if key[1] == 'Sunny':
            sunny.append(key)
        elif key[1] == 'Rainy':
            rainy.append(key)
        elif key[1] == 'Cloudy':
            cloudy.append(key)
        my_list.append(key)
    sunny.sort()
    rainy.sort()
    cloudy.sort()
    all_whether = sunny + cloudy + rainy
    arr = []
    for key, value in all_whether:
        arr.append(f"{key} - {value}")
    return '\n'.join(arr)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))


