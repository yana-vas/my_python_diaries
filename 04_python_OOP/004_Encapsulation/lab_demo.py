# Lab exercises

# problem 1

# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# person = Person("George", 32)
# print(person.get_name())
# print(person.get_age())

# problem 2

# class Mammal:
#     __kingdom = "animals"
#
#     def __init__(self, name, type, sound):
#         self.name = name
#         self.type = type
#         self.sound = sound
#
#     def get_kingdom(self):
#         return self.__kingdom
#
#     def make_sound(self):
#         return f"{self.name} makes {self.sound}"
#
#     def info(self):
#         return f"{self.name} is of type {self.type}"
#
#
# mammal = Mammal("Dog", "Domestic", "Bark")
# print(mammal.make_sound())
# print(mammal.get_kingdom())
# print(mammal.info())

# --- ppt lab exercise ---

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value <= 18:
#             self.__age = 18
#         self.__age = value
#
#
# p = Person("Yana", 16)
# print(p.age)

# problem 3

import re

#
# class Profile:
#
#     def __init__(self, username: str, password: str):
#         self.username = username
#         self.password = password
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, value):
#         if not 5 <= len(value) <= 15:
#             raise ValueError("The username must be between 5 and 15 characters.")
#         self.__username = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         if len(value) < 8 or not any(char.isupper() for char in value) or not any(char.isdigit() for char in value):
#             # not re.search(r'[A-Z]', password) or not re.search(r'\d', password)
#             raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#         self.__password = value
#
#     def __str__(self):
#         return f"You have a profile with username: \"{self.username}\" and password: {'*'*len(self.password)}"
#
#
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)


# problem 4

# class EmailValidator:
#
#     def __init__(self, min_length, mails, domains):
#         self.min_length = min_length
#         self.mails = mails
#         self.domains = domains
#
#     def __is_name_valid(self, name):
#         return len(name) >= self.min_length
#
#     def __is_mail_valid(self, mail):
#         return mail in self.mails
#
#     def __is_domain_valid(self, domain):
#         return domain in self.domains
#
#     def validate(self, email):
#         data = email.split('@')
#         name = data[0]
#         mail, domain = data[1].split('.')
#
#         return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)
#         # pe77er@gmail.com


# mails = ["gmail", "softuni"]
# domains = ["com", "bg"]
# email_validator = EmailValidator(6, mails, domains)
# print(email_validator.validate("pe77er@gmail.com"))
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))

# problem 5

class Account:

    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))