import re

pattern = r"(www.([a-zA-Z0-9\-]+)(\.[a-z]+)+)"
text = input()
links = []
while text:
    match = re.findall(pattern, text)
    if len(match) > 0:
        print(match[0][0])
    text = input()