import re

text = input()
pattern = r"[\@\#]+([a-z]{3,})[\@\#]+[^a-zA-Z0-9]+[/]+(\d+)[/]+"
# eggs = list()
# count = list()
# amount = 0

matches = re.findall(pattern, text)

for match in matches:
    color = match[0]
    amount = int(match[1])
    # eggs.append(color)
    # count.append(amount)
    # text = input()

    print(f"You found {amount} {color} eggs!")