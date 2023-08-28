import re

n = int(input())

text = input()
name_pattern = r"(\@[a-zA-Z]+\|)"
names = re.findall(name_pattern, text)