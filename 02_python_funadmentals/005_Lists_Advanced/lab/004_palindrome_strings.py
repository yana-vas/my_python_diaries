input_words = input().split(' ')
palindrome_word = input()
filtered = [word for word in input_words if word == ''.join(reversed(word))]
counter_palindrome = [word for word in filtered if word == palindrome_word]
print(filtered)
print(f"Found palindrome {len(counter_palindrome)} times")
