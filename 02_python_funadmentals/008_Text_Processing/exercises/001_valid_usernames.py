usernames = input().split(', ')
valid_usernames = []

for user in usernames:
    is_valid = False
    if 3 <= len(user) <= 16:
        for char in user:
            if char.isalpha() or char.isdigit() or char == '-' or char == '_':
                is_valid = True
            else:
                is_valid = False
                break
    if is_valid:
        valid_usernames.append(user)
for username in valid_usernames:
    print(username)
