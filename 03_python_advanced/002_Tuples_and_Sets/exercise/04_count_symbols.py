text = sorted((input()))
letters = {}

for l in text:
    if l not in letters:
        letters[l] = 0
    letters[l] += 1

for char, appearance in letters.items():
    print(f"{char}: {appearance} time/s")
