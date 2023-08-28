def playfair_decode(message, keyword=None):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""

    # create the tableau
    if keyword:
        # use the keyword to fill the tableau
        tableau = []
        for letter in keyword + alphabet:
            if letter not in tableau:
                tableau.append(letter)
    else:
        # use the regular alphabet to fill the tableau
        tableau = [letter for letter in alphabet]

    # divide the message into digrams
    digrams = [message[i:i + 2] for i in range(0, len(message), 2)]

    # decode the digrams
    for digram in digrams:
        # find the positions of the letters in the tableau
        pos1 = (tableau.index(digram[0]) // 5, tableau.index(digram[0]) % 5)
        pos2 = (tableau.index(digram[1]) // 5, tableau.index(digram[1]) % 5)

        # if both letters are in the same row, replace them with the letters to their left
        if pos1[0] == pos2[0]:
            decoded_digram = tableau[pos1[0] * 5 + (pos1[1] - 1) % 5] + tableau[pos2[0] * 5 + (pos2[1] - 1) % 5]

        # if both letters are in the same column, replace them with the letters above them
        elif pos1[1] == pos2[1]:
            decoded_digram = tableau[((pos1[0] - 1) % 5) * 5 + pos1[1]] + tableau[((pos2[0] - 1) % 5) * 5 + pos2[1]]

        # if the letters are in different rows and columns, replace them with the letters on the same row but in the columns of the other letter
        else:
            decoded_digram = tableau[pos1[0] * 5 + pos2[1]] + tableau[pos2[0] * 5 + pos1[1]]

        decoded_message += decoded_digram

    return decoded_message


message = "iskyjqcwtkfw"
keyword = "secret"
decoded_message = playfair_decode(message, keyword)
print(decoded_message)