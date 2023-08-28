words = input().split(' ')
filtered_words = list(filter(lambda word: len(word) % 2 == 0, words))
[print(current_word) for current_word in filtered_words]