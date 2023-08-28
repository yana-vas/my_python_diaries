phone_book = {}
while True:
    contact = input()
    if contact.isdigit():
        break
    contact = contact.split('-')
    name = contact[0]
    phone_number = contact[1]
    phone_book[name] = phone_number
for i in range(int(contact)):
    searched_name = input()
    if searched_name in phone_book:
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")