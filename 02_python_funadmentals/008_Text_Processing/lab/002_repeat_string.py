input_data = input().split(' ')

repeated_text = ''
for word in input_data:
    for i in range(len(word)):
        repeated_text += word

print(repeated_text)