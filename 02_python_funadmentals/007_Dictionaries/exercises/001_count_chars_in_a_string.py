import collections

text = list(input())
occurrences = collections.Counter(text)
for char in occurrences:
    if char != ' ':
        print(f"{char} -> {occurrences[char]}")