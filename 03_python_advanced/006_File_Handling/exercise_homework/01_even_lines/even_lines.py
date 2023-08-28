symbol = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            line = ' '.join(reversed(line.strip().split()))
            for char in symbol:
                line = line.replace(char, '@')
            print(line)