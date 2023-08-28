"""
The Hill cipher is a method of encryption that uses linear algebra to encode messages. It is a polyalphabetic substitution cipher, meaning that it uses multiple substitution alphabets to encode the message.

To encode a message using the Hill cipher, the following steps are taken:

Choose a key matrix (a 2x2 or 3x3 matrix of integers) that will be used to encode the message.
Divide the message into groups of letters (known as "blocks") that are the same size as the key matrix. If the message is not a multiple of the key matrix size, pad it with extra letters (such as "x" or "z") to make it fit.
For each block, multiply the block by the key matrix (modulo 26, to wrap around the alphabet). The resulting matrix is the encoded block.
Repeat this process for each block in the message.
To decode a message that has been encoded using the Hill cipher, the inverse of the key matrix is used to multiply the encoded blocks. This effectively "undoes" the encoding process, allowing the original message to be recovered.

The Hill cipher is relatively secure, as long as the key matrix is chosen randomly and kept secret. However, it can be broken using techniques such as linear algebra and brute force attacks, so it is not considered a strong encryption method for modern use.




"""

import numpy as np


def hill_encrypt(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = ""

    # pad the message if necessary
    block_size = key.shape[0]
    if len(message) % block_size != 0:
        message += "x" * (block_size - len(message) % block_size)

    # divide the message into blocks
    blocks = [message[i:i + block_size] for i in range(0, len(message), block_size)]

    # encode the blocks
    for block in blocks:
        # convert the block to a matrix
        block_matrix = np.array([alphabet.index(letter) for letter in block])

        # multiply the block matrix by the key matrix
        encoded_matrix = np.mod(np.matmul(block_matrix, key), 26)

        # convert the encoded matrix back to a string
        encoded_block = "".join([alphabet[i] for i in encoded_matrix])

        encoded_message += encoded_block

    return encoded_message


import numpy as np


def hill_decrypt(encoded_message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""

    # divide the encoded message into blocks
    block_size = key.shape[0]
    blocks = [encoded_message[i:i + block_size] for i in range(0, len(encoded_message), block_size)]

    # decode the blocks
    inverse_key = np.linalg.inv(key)
    for block in blocks:
        # convert the block to a matrix
        block_matrix = np.array([alphabet.index(letter) for letter in block])

        # multiply the block matrix by the inverse of the key matrix
        decoded_matrix = np.mod(np.matmul(block_matrix, inverse_key), 26)

        # convert the decoded matrix back to a string
        decoded_block = "".join([alphabet[i] for i in decoded_matrix])

        decoded_message += decoded_block

    return decoded_message





def hill_encrypt2(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = ""

    # pad the message if necessary
    block_size = key.shape[0]
    if len(message) % block_size != 0:
        message += "x" * (block_size - len(message) % block_size)

    # divide the message into blocks
    blocks = [message[i:i + block_size] for i in range(0, len(message), block_size)]

    # encode the blocks
    for block in blocks:
        # convert the block to a matrix
        block_matrix = np.array([alphabet.index(letter) for letter in block])

        # multiply the block matrix by the key matrix
        encoded_matrix = np.mod(np.matmul(block_matrix, key), 26)

        # convert the encoded matrix back to a string
        encoded_block = "".join([alphabet[i] for i in encoded_matrix])

        encoded_message += encoded_block

    return encoded_message


encoded_message = "Hfopz, Wflnk!"
key = np.array([[7, 8], [5, 7]])
decoded_message = hill_decrypt(encoded_message, key)
print(decoded_message)

message = "Hello, World!"
key = np.array([[7, 8], [5, 7]])
encoded_message = hill_encrypt2(message, key)
print(encoded_message)
