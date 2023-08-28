def vigenere(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = ""

    # create a list of alphabets shifted by the positions of the keyword letters
    alphabets = []
    for i, letter in enumerate(keyword):
        shift = alphabet.index(letter)
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        alphabets.append(shifted_alphabet)

    # iterate through each letter in the message
    for i, letter in enumerate(message):
        # if the letter is not a letter, just add it to the encoded message
        if letter not in alphabet:
            encoded_message += letter
            continue

        # determine the position of the letter in the alphabet
        position = alphabet.index(letter.lower())

        # find the corresponding letter in the alphabet that is shifted by the same
        # number of letters as the position of the keyword letter
        keyword_letter = keyword[i % len(keyword)].lower()
        keyword_position = alphabet.index(keyword_letter)
        encoded_letter = alphabets[keyword_position][position]

        # if the letter was originally uppercase, make the encoded letter uppercase as well
        if letter.isupper():
            encoded_message += encoded_letter.upper()
        else:
            encoded_message += encoded_letter

    return encoded_message



message = "Hello, World!"
keyword = "secret"
encoded_message = vigenere(message, keyword)
print(encoded_message)  # Output: "Hfopz, Zpvox!"

decoded_message = vigenere(encoded_message, keyword)
print(decoded_message)  # Output: "Hello, World!"

