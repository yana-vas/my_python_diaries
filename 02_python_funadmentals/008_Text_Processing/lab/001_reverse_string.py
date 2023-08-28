word = input()
while word != 'end':
    # print(word[::-1])
    reversed_word = ''.join(list(reversed(word)))
    print(f"{word} = {reversed_word}")
    word = input()