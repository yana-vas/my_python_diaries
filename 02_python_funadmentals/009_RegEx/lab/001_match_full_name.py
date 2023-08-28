import re

regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
names = input()
filtered_names = re.findall(regex, names)
print(" ".join(filtered_names))

