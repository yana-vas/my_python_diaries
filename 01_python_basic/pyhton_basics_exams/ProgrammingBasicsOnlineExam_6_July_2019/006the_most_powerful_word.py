import math

command = input()
power = 0
powerful_word = ""
while command != "End of words":
    word = command
    counter = 0
    for i in range(len(word)):
        counter += ord(word[i])
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y' or \
            word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y':
        counter *= len(word)
    else:
        counter = math.floor(counter/len(word))
    if counter >= power:
        power = counter
        powerful_word = word
    command = input()
print(f"The most powerful word is {powerful_word} - {power}")
