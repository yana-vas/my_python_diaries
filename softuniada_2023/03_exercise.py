input_data = input()
counts = []
count = 0

i = 0
while i < len(input_data)-1:
    char = input_data[i]
    next_char = input_data[i + 1]
    if char + next_char == '()':
        count += 2
        i += 1
    else:
        counts.append(count)
        count = 0
    i += 1

counts.append(count)
print(max(counts))