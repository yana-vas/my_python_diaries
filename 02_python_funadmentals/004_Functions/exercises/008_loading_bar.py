number = int(input())


def loading_bar(percent):
    bar = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    for i in range(percent//10):
        bar[i] = '%'
    load_bar = ''.join(bar)
    if percent == 100:
        print(f"{percent}% Complete!")
        print(f'[{load_bar}]')
    else:
        print(f'{percent}% [{load_bar}]')
        print("Still loading...")


loading_bar(percent=number)
