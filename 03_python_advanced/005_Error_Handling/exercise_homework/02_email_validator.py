class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


command = input()
while command != 'End':
    email = command
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif email.count('@') == 1:
        username, domain = email.split('@')
    else:
        command = input()
        continue

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if (domain.split('.'))[-1] not in ['bg', 'com', 'org', 'net']:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    command = input()
