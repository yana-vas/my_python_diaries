import string

rows, cols = [int(x) for x in input().split(' ')]

alphabet = list(string.ascii_lowercase)
matrix = []

for r_index in range(rows):
    line = []
    for c_index in range(cols):
        first_letter = alphabet[r_index]
        last_letter = alphabet[r_index]
        middle_letter = alphabet[r_index+c_index]
        palindrome = first_letter + middle_letter + last_letter
        line.append(palindrome)
    print(*line)
