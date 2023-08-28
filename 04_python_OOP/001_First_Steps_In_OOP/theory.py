# Creating Class
# The keyword class defines a new category
class Snake:
    pass
# We define the state of the object using attributes
class Snake:
    def __init__(self, specie, size, price):  # special method
        self.specie = specie  # attribute
        self.size = size  # attribute
        self.price = price  # attribute

# _num = 10 - подсигуряваш се че искаш да проемниш стойността на _num извън класът
# __num = 10 - не можеш да променяш стойността на __num извън класът

# __repr__() - returns the object representation in string format.
# This method is called when repr() function is invoked on the object.
# If possible, the string returned should be a valid Python expression that can be used to reconstruct the object again.

# Example
class Test:
    def __init__(self, counter):
        self.counter = counter

    def __repr__(self):
        return f"Remaining: {self.counter}"


test = Test(5)
print(test)  # Remaining: 5


# OOP is a programming paradigm
# Provides a means of structuring programs so that properties and behaviors are bundled intoindividual objects
# Objects are at the center of the OOP paradigm
# An object-oriented program consist of objects that interact with each other

# Class definition
# A class is like a blueprint for creating objects
# Classes provide a means of bundling data and functionality together
# Each class instance can have attributes attached to it
# Class instances can also have methods for modifying its state

# The __init__() Function

# All classes create objects, and all objects contain characteristics called attributes
# The __init__() method initializes an object's initial attributes by giving them their default value
# The double leading and trailing underscore is used for special variables or methods

# The Self Variable

# The self parameter is a reference to the current instance of the class
# Used to access variables that belong to the class
# When defining an instance method, the first parameter of the method should always be self

# Class Example
# Create a class Person that has, first name, last name and age

class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


# When a parameter is optional, put a default value that it should have

# Object Definition

# Instance is concrete object of the category of the class
# A class is like a form or template
# It defines the needed information
# You can fill out multiple copies, but without the form you will not know the required information

# Object Example
# Using the Person class we created, here we have an example of the instance of that class
me = Person("Peter", "Johnson", 25)
print(me.first_name)  # Peter
print(me.last_name)  # Johnson
print(me.age)  # 25

# Modifying Attributes
# You can change the values of the attributes of an object after initialization
me = Person("Peter", "Johnson", 25)
me.age += 1
print(me.age)  # 26


class MyClass:
    # Class attributes are defined outside of constructor
    class_attr = 0

    def __init__(self, inst):
        # Instance attributes are defined in the constructor
        self.instance_attr = inst


obj = MyClass(1)
print(obj.class_attr)  # outputs 0
print(obj.instance_attr)  # outputs 1
print(MyClass.class_attr)  # outputs 0
print(MyClass.instance_attr)  # raises AttributeError

# The change will be made only for that instance of the class

# Class Attributes
# While instance attributes are specific to each object, class attributes are the same for all instances
class Person:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


me = Person("Peter", 25)  # me.species = "mammal"
you = Person("John", 44)  # you.species = "mammal"


# Instance Methods

# Instance methods are defined inside a class and are used to get the contents of an instance
# They can also be used to perform operations with the attributes of our objects
# Like the __init__ method, the first argument should  always be self

# Code Example
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


me = Person("Peter", "Johnson", 64)
print(me.get_full_name())  # Peter Johnson
