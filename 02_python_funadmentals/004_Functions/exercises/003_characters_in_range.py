first_char_value = input()
second_char_value = input()

characters_list = []


def character_range(char_1, char_2):
    for i in range(ord(char_1)+1, ord(char_2)):
        characters_list.append(chr(i))
    return ' '.join(characters_list)


print(character_range(char_1=first_char_value, char_2=second_char_value))
