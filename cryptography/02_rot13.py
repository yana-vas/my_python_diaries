"""
ROT 13 is a simple substitution cypher that involves shifting each letter of the alphabet by 13 places. For example, the letter "A" would become "N", "B" would become "O", and so on.

To encode a message using ROT 13, the following steps are taken:

Split the message into individual letters.
For each letter, determine its position in the alphabet (A=1, B=2, etc.).
Shift the letter by 13 places. For example, if the letter is "A", it becomes "N".
If the shifted letter is beyond the 26th letter of the alphabet (Z), wrap around to the beginning of the alphabet. For example, if the letter is "N", it becomes "A".
Repeat this process for each letter in the message.
To decode a message that has been encoded using ROT 13, the same process is followed, except the shift is reversed (i.e. the letter is shifted back 13 places instead of forward). This effectively "undoes" the encoding process, allowing the original message to be recovered.
"""


def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = ""

    # iterate through each letter in the message
    for letter in message:
        # if the letter is not a letter, just add it to the encoded message
        if letter not in alphabet:
            encoded_message += letter
            continue

        # determine the position of the letter in the alphabet
        position = alphabet.index(letter.lower())

        # shift the letter by 13 places
        shifted_position = (position + 13) % 26

        # if the letter was originally uppercase, make the encoded letter uppercase as well
        if letter.isupper():
            encoded_message += alphabet[shifted_position].upper()
        else:
            encoded_message += alphabet[shifted_position]

    return encoded_message

"""
To use this function, simply call it with the message you want to encode as an argument. For example:
"""

message = "Hello, World!"
encoded_message = rot13(message)
print(encoded_message)  # Output: "Uryyb, Jbeyq!"

"""
To decode a message that has been encoded using ROT 13, you can simply call the function again with the encoded message as an argument. This will "undo" the encoding and return the original message.
"""

decoded_message = rot13(encoded_message)
print(decoded_message)  # Output: "Hello, World!"
