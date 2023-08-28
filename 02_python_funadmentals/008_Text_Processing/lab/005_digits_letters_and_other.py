input_data = input()
character = ''
digits = ''
letters = ''
for char in input_data:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        character += char
print(digits)
print(letters)
print(character)
