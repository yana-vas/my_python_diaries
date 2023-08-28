import re

text = input()
pattern = r"(([:]{2}|[*]{2})([A-Z][a-z]{2,})\2)"
cool_threshold = 1
cool_emojis = []
matches = re.findall(pattern, text)
for char in text:
    if char.isdigit():
        cool_threshold *= int(char)
for match in matches:
    emoji = str(match[2])
    threshold = 0
    for letter in emoji:
        threshold += ord(letter)
    if threshold > cool_threshold:
        cool_emojis.append(match[0])
if len(matches) > 0:
    print(f"Cool threshold: {cool_threshold}")
    print(f"{len(matches)} emojis found in the text. The cool ones are:")
    for cool_emoji in cool_emojis:
        print(cool_emoji)

