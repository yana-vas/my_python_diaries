# self.__class__.__name__ - get the name of the class

# __init__() - Creates objects with instances, customized to a specific initial state
# self Parameter - self is used to represent the instance of the class. It binds the attributes with the given arguments

# Attributes - Data and procedures that "belong" to the class.
# Valid attribute names are the ones in the class's namespace

# Instance Methods - Define the behavior of the object
# -> първия параметър е self
class Example:
    def my_instance_method(self):
        return "This is an example of instance method"
# The instance object is passed as a first argument of the method - using "self"  by convention
class MyClass:

    def say_hello(self):
        return 'Hello'

x = MyClass()
print(x.say_hello())        # conventional way -> Hello
print(MyClass.say_hello(x))  # equivalent to -> Hello

# Special/ Dunder Methods - Built-in methods that you can define to add "magic" to your classes
# Surrounded by double underscores e.g., __init__
# __str__() - returns a printable string representation of any user defined class

class Person:
    def __str__(self):
        return 'This message is returned, when calling the object'


person = Person()

print(person)
print(person.__str__())
print(str(person))


# __repr__() - returns a machine-readable representation of any user defined class

class MyClass:
    def __repr__(self):
        return 'This is My Class'


my_instance = MyClass()

print(repr(my_instance))  # This is My Class
print(my_instance.__repr__())  # This is My Class
print(my_instance)  # This is My Class


# use print() only when __repr__() returns string

# Methods -We could change the state of the object using methods
class Dog:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name


x = Dog("Max")
x.change_name("Rex")
print(x.name)  # Rex


# Data Attributes - Values which are stored internally and are unique to that object

# They define the state of the object
# There are two types of data attributes:
#   -> Instance variables - unique to each instance
#   -> Class variables - shared by all instances of the class
class Laptop:
    brand = "Dell"            # class variable

    def __init__(self, name):
        self.name = name      # instance variable

first_laptop = Laptop("Latitude 5300")
second_laptop = Laptop("Inspiron 15")
print(first_laptop.brand == second_laptop.brand)  # True
print(first_laptop.name == second_laptop.name)   # False

#   -> Instance variables - independent from one instance to the other
#   -> Class variables - Modifying a class variable affects all object instances at the same time
class Dog:
    tricks = []     # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

poodle = Dog("Bella")
beagle = Dog("Max")
poodle.tricks.append('roll over')
print(beagle.tricks) # shared by all dogs ['roll over']


# class attribute


# first_laptop = Laptop("Latitude 5300")
# second_laptop = Laptop("Inspiron 15")
# Laptop.brands = ["changed from the class"]
# print(first_laptop.brands) -> ['changed from the class']
# print(second_laptop.brands) -> ['changed from the class']
class Laptop:
    brands = ["Dell", 'Asos']  # class variable

    def __init__(self, name):
        self.name = name  # instance variable


first_laptop = Laptop("Latitude 5300")
second_laptop = Laptop("Inspiron 15")
print(first_laptop.brands)
print(second_laptop.brands)
first_laptop.brands = ['First laptop brand']  # instance attribute
# the list "brands" will be changed only for first_laptop
# You can imagine that in the __init__ method is added self.brands = ['First laptop brand'])
print(first_laptop.brands)
print(second_laptop.brands)
Laptop.brands = ["changed from the class"]  # class attribute
print(first_laptop.brands)  # first_laptop is changed in the local scope, so when searching for brands it will find
# the brands in the __init__ method, where you can find something like this -> self.brands = ['First laptop brand']
print(second_laptop.brands)

# Input:
# ['Dell', 'Asos']
# ['Dell', 'Asos']
# ['First laptop brand']
# ['Dell', 'Asos']
# ['First laptop brand']
# ['changed from the class']

# class attribute могат да бъдат извикани директно през името на класа, без да ни е нужна инстанция
# class attribute is shared within all instances
# -> Laptop.brand = ['changed from the class'] всички инстанции вече са модифицирани т.е.
# first_laptop.brands = ['changed from the class'] и second_laptop.brands = ['changed from the class']


# Special Data Attributes

# The __doc__ Attribute - Provides a documentation of the object as a string
class MyClass:
    """This is MyClass."""

    def example(self):
        """This is the example module of MyClass."""

print(MyClass.__doc__) # This is MyClass.
print(MyClass.example.__doc__)
# This is the example module of MyClass.

# The __dict__ Attribute - This is a dictionary containing a module's symbol table
class MyClass:
    class_variable = 1

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

first = MyClass(2)
second = MyClass(3)

print(MyClass.__dict__) # {'__module__': '__main__', ... }
print(first.__dict__)     # { 'instance_variable': 2 }
print(second.__dict__)    # { 'instance_variable': 3 }


# Summary
#  Instance Attributes are unique to each object, (an instance is another name for an object)
# Instance objects are individual objects of a class
# Methods are functions that belong to an object
# Instance variables are unique to each instance
# Class Variables are shared by all instances
