import re
text = input()

matched_words = []
pattern = r"([\@\#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"

matches = re.findall(pattern, text)
for match in matches:
    first_word = match[1]
    second_word = match[2]
    if first_word == second_word[::-1] and first_word[::-1] == second_word:
        matched_words.append(first_word + ' <=> ' + second_word)

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if len(matched_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(matched_words))
