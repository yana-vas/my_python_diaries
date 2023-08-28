password_input = input()


def password_validator(text):
    is_password_valid = False
    output_list = []
    if 6 <= len(text) <= 10:
        is_password_valid = True
    else:
        output_list.append("Password must be between 6 and 10 characters")
    if text.isalnum():
        is_password_valid = True
    else:
        output_list.append("Password must consist only of letters and digits")
        is_password_valid = False
    digit_counter = 0
    for char in text:
        if char.isdigit():
            digit_counter += 1
    if digit_counter >= 2:
        is_password_valid = True
    else:
        is_password_valid = False
        output_list.append("Password must have at least 2 digits")
    if is_password_valid:
        output_list.append("Password is valid")
    for elem in output_list:
        return elem


print(password_validator(password_input))

