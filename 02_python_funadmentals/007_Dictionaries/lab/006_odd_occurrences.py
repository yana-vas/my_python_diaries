import collections
words = input().split(' ')
words = [word.lower() for word in words]
occurrences = collections.Counter(words)
to_print = []
for x in occurrences:
    if occurrences[x] % 2 != 0:
        to_print.append(x)
print(' '.join(to_print))
