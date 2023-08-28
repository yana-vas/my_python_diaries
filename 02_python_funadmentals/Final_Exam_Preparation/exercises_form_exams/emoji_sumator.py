import re

text = input()
total_power = 0
pattern = r"(?<=\s):([a-z]{4,}):(?=\s|\,|\.|\!|\?)"
matches = re.findall(pattern, text)
for match in matches:
    emoji = match
    for char in emoji:
        total_power += ord(char)
emoji_code = input().split(':')
secret_emoji = ''
for num in emoji_code:
    secret_emoji += chr(int(num))
if secret_emoji in matches:
    total_power *= 2
if len(matches) > 0:
    print(f"Emojis found: {', '.join(matches)}")
print(f"Total Emoji Power: {total_power}")

