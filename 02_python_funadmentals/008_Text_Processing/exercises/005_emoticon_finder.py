text = input()
emoticons = []
for i in range(len(text)):
    letter = text[i]
    if letter == ':':
        emoticons.append(letter+text[i+1])
for emoticon in emoticons:
    print(emoticon)