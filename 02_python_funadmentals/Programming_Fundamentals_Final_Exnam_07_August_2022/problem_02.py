import re

n = int(input())
pattern = r"^([\$|\%])([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"
for i in range(n):
    text = input()
    match = re.findall(pattern, text)
    if match:
        match = list(match[0])
        tag = match[1]
        new_str = chr(int(match[2])) + chr(int(match[3])) + chr(int(match[4]))
        print(f"{tag}: {new_str}")
    else:
        print("Valid message not found!")