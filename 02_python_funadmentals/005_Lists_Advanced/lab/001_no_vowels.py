text = input()
vowels = 'aoueiAOUEI'
filtered = ''.join([letter for letter in text if letter not in vowels])
print(filtered)