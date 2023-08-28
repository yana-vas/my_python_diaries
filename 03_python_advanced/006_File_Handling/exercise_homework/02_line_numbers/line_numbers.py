import re

with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for row, line in enumerate(input_file):
        len_punctuation = len(re.findall("[!\"#$%&'()*+,\-./:;<=>?@[\]^_`{|}~]", line))
        len_letters = len(re.findall("[A-Za-z]", line))
        output_file.write(f'Line {row + 1}: {line.strip()} ({len_letters})({len_punctuation})\n')
