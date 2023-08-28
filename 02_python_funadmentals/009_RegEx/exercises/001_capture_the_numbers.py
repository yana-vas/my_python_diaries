import re

pattern = r'\d+'
input_data = input()

numbers = ''
while True:
    if input_data:
        match = re.findall(pattern, input_data)
        if len(match) != 0:
            numbers += ' '.join(match) + ' '
    else:
        break
    input_data = input()
print(numbers)


