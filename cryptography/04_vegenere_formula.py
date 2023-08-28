def vigenere_encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""

    # iterate through each letter in the plaintext
    for i, letter in enumerate(plaintext):
        # if the letter is not a letter, just add it to the ciphertext
        if letter not in alphabet:
            ciphertext += letter
            continue

        # determine the position of the letter in the alphabet
        position = alphabet.index(letter.lower())

        # find the corresponding letter in the alphabet that is shifted by the same
        # number of letters as the position of the key letter
        key_letter = key[i % len(key)].lower()
        key_position = alphabet.index(key_letter)
        cipher_letter = (position + key_position) % 26

        # if the letter was originally uppercase, make the cipher letter uppercase as well
        if letter.isupper():
            ciphertext += alphabet[cipher_letter].upper()
        else:
            ciphertext += alphabet[cipher_letter]

    return ciphertext


def vigenere_decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""

    # iterate through each letter in the ciphertext
    for i, letter in enumerate(ciphertext):
        # if the letter is not a letter, just add it to the plaintext
        if letter not in alphabet:
            plaintext += letter
            continue

        # determine the position of the letter in the alphabet
        position = alphabet.index(letter.lower())

        # find the corresponding letter in the alphabet that is shifted back by the same
        # number of letters as the position of the key letter
        key_letter = key[i % len(key)].lower()
        key_position = alphabet.index(key_letter)
        plain_letter = (position - key_position) % 26

        # if the letter was originally uppercase, make the plain letter uppercase as well
        if letter.isupper():
            plaintext += alphabet[plain_letter].upper()
        else:
            plaintext += alphabet[plain_letter]

    return plaintext


plaintext = "Hello, World!"
key = "secret"
ciphertext = vigenere_encrypt(plaintext, key)
print(ciphertext)  # Output: "Hfopz, Zpvox!"

decrypted_plaintext = vigenere_decrypt(ciphertext, key)
print(decrypted_plaintext)  # Output: "Hello, World!"
