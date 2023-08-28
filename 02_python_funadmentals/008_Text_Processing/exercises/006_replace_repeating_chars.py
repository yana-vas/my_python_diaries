text = input()
sb = []
for i in range(len(text)-1):
    if text[i] != text[i + 1]:
        sb.append(text[i])
sb.append(text[-1])
print(''.join(sb))