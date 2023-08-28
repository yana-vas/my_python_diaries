import re

secret_message = []
words = input().split(' ')
for current_word in words:
    first_letter = int(''.join(re.findall('\d+', current_word)))
    current_word = result = chr(first_letter) + ''.join([i for i in current_word if not i.isdigit()])
    current_word = list(''.join(current_word))
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    secret_message.append(''.join(current_word))
print(' '.join(secret_message))
