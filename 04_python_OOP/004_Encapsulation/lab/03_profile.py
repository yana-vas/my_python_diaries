import re


class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        is_valid = 5 <= len(value) <= 15
        if not is_valid:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # is_upper_presented = any([True for char in value if char.isupper()])
        # is_digit_presented = any([True for char in value if char.isdigit()])

        my_regex = re.search('\d.*[A-Z].*|[A-Z].*\d.*', value)
        is_valid = len(value) >= 8 and my_regex != None
        if not is_valid:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile.username)
