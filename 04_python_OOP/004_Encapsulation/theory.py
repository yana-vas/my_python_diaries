# Защо да използваме енкапсулация?
# за да скрем някакви неща само за класа/наследника
# за да извършим валидация

# public - видимо от всички
# _protected - видимо само от наследници и класа, в който са дефинирани
# __private - видимо само в конкретния клас

# private атрибути - означават се с –– пред името на атрибута; видими са само в рамките на класа(в Python може да се достъпят дори извън класа)
# protected атрибути - видими само в класа, в който са дефинирани и в дъщерните класове (класа наследник)

# Python е със слаба енкапсулация и може да правиш каквото си поискаш с private и protected

# енкапсулация - да енкапсулираме нещо, така че да го предпазиме
# Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit

class CreditCard:
    def __init__(self, number, exp_date, cvc, name, pin):
        self.number = number
        self.exp_date = exp_date
        self.cvc = cvc
        self.name = name
        self.__pin = pin  # pin не може да се достъпва извън класа (private attribute)
        # When naming an attribute with two leading underscores, it invokes name mangling
        # Used to show that the variable should not be accessed outside the class

        # Protected
        # No access outside of the class or subclasses
        self._this_is_protected = True
        # Private
        # No access outside of the class
        self.__this_is_private = True

    def __is_pin_correct(self, pin):
        return self.__pin == pin

    def change_pin(self, old_pin, new_pin):  # setter
        if self.__is_pin_correct(old_pin):
            self.__pin = new_pin
            return
        raise ValueError("Old pin is not correct")

    def get_pin(self):  # getter
        return self.__pin

    def set_pin(self, pin):  # setter
        if len(pin) == 4:
            self.__pin = pin
        else:
            raise ValueError("PIN have to be 4 digits")



card = CreditCard(12345, '2022-10', 345, "Test Name", 7887)
card.__pin = 2468  # won't change because it is name mangled
card.get_pin()  # 7887

# В Python няма нищо private, тоест дори атрибута да ни е private (__name) може да го достъпим по следния начин:
card.change_pin(7887, 1234)
print(card._CreditCard__pin)  # _ClassName__attributeName


# GETTERS and SETTER
# defining getters and setters is using properties
# By defining properties, you can change the internal implementation of a class without affecting the program

class Person:
    def __init__(self, age=0):
        self.age = age

    # props - автоматично ти прави setter & getter
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age < 18: self.__age = 18  # слагаме __ пред атрибута, за да не влизаме в рекурсия
        else: self.__age = age


person = Person(25)
print(person.age)	# 25
person.age = 10  # когато слагаме стойност на променлива (атрибут), влизаме в setter, освен ако атрибутът не е private
# в този случай age (value) е 10
print(person.age)	# влизаме в property декоратора
# 18


class Car:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def drive(self):
        print('driving max speed ' + str(self.max_speed))

    @property   # Implement properties only if needed
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value > 447:
            value = 447
        self.__max_speed = value

red_car = Car(200)
red_car.drive()             # driving max speed 200
red_car.max_speed = 512     # changes the speed to 447
red_car.drive()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # когато видим = отиваме при setter, ако има такъв за дадения атрибут

    def get_age(self):  # това прави същото, което прави гетърът (@property)
        return self.age  # когато викаме self.age отиваме при гетъра (@property), ако имаме такъв
    
    # You should use Python properties to apply rules to an attribute
    @property
    def age(self):  # всеки метод с декоратор @property става атрибут
        return self.__age  # атрибут създаден от сетъра

    @age.setter
    def age(self, value):
        if value <= 0:
            raise Exception("Age must be greater than zero")    # An exception will be thrown on any attempt to violate the rule
        self.__age = value


p = Person('Emily', 22)
print(p.age) # когато искаме да вземем дадена стойност отиваме при гетъра (@property), т.е. когато нямаме = използваме гетър, а ако имаме - сетър


# ако не искате да минавате през декораторите (setter & getter), атрибутът тябва да е private
# с @ се обозначават декоратори
# от property се очаква return, а от setter не се очаква да има return
# property се явява геър. Логиката се изпълнява първо през сетъра и след това през (@property) гетъра


# Name Mangling a Method - a class method that should only be called from inside the class where it is defined

class Person:
    def __init__(self):
        self.first_name = 'Peter'
        self.last_name = 'Parker'

    def __full_name(self):
        return f'{self.first_name} {self.last_name}'

    def info(self):
        return self.__full_name()


person = Person()
print(person.info())	              # Peter Parker
print(person.__full_name())	   # AttributeError
print(person._Person__full_name())  # Peter Parker


# Built-in Functions for Accessing Attributes
# getattr() - used to access the attribute of an object -> Returns the value of the named attribute
# The method takes multiple parameters:
# Object
# Name
# Default (optional)


class Person:
    def __init__(self, name):
        self.name = name

person = Person('Peter')
print(getattr(person, 'name'))         # True  (връща ни дали този обект има такъв атрибут)
print(getattr(person, 'age'))          # AttributeError
print(getattr(person, 'age', 'None'))  # None
#             object   name  default(optional)

# __getattr__() - Called when an attribute lookup has not found the attribute in the usual places
# The method takes one parameter – the name of the attribute

class Dog:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):  # ако нямахме този метод, щеше да ни излезе AttributeError
        return 'Bla, Bla'


dog = Dog('Ralph')
print(dog.color)  # Bla, Bla  (това излиза, защото НЯМАМЕ атрибут 'color')
print(getattr(dog, 'color'))  # Bla, Bla  (това излиза, защото НЯМАМЕ атрибут 'color')
print(getattr(dog, 'size'))   # Bla, Bla  (това излиза, защото НЯМАМЕ атрибут 'size')
print(getattr(dog, 'name'))   # Ralph  (това излиза, защото  ИМАМЕ атрибут 'name')
print(dog.name)   # Ralph  (това излиза, защото  ИМАМЕ атрибут 'name')


# hasattr() - checks if an attribute exist or not
# Returns True if an object has the given named attribute and False if it does not
# The method takes two parameters: Object and Name

class Person:
    def __init__(self, name):
        self.name = name


person = Person('Peter')
print(hasattr(person, 'name')) # True
print(hasattr(person, 'age'))  # False


# setattr() - used to set the value of the attribute -> Returns None
# The method takes three parameters: Object, Name and Value
# дори да няма такъв атрибут, чрез setattr() ние създаваме такъв и му даваме стойност


class Person:
    def __init__(self, name):
        self.name = name


person = Person('Peter')
print(person.name)                        # Peter
print(setattr(person, 'name', 'George'))  # None
print(person.name)                        # George
print(setattr(person, 'age', 21))         # None
print(person.age)                         # 21


# __setattr__() - Called when an attribute assignment is attempted
# The method takes two parameters:
#     => The name of the attribute
#     => The value we want to assign to the attribute

class Phone:
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value.upper()


phone = Phone()
phone.color = 'black'
print(phone.color)  # BLACK


# delattr() - deletes an attribute from the object
# If you are accessing the attribute after deleting it raises AttributeError
# The method takes two parameters: Object and Name

class Person:
    def __init__(self, name):
        self.name = name


person = Person('Peter')
print(person.name)                 # Peter
print(delattr(person, 'name'))     # None
# del person.name
print(person.name)                 # AttributeError


# __delattr__() - Called when an attribute deletion is attempted
# The method takes one parameter: The  name of the attribute
# It should only be implemented if del obj.name is meaningful for the object

class Phone:
    def __delattr__(self, attr):
        del self.__dict__[attr]
        print(f"'{str(attr)}' was deleted")


phone = Phone()
phone.color = 'black'
del phone.color  # 'color' was deleted



# SUMMARY
# Encapsulation is packing of data and functions into a single component
# Name mangling is used for attributes that one class does not want subclasses to use
# The property decorator is the pythonic way of using getters and setters
# We could use built-in functions for accessing attributes
