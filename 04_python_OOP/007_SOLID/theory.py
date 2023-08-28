# Single Responsibility - Each class is responsible for only one thing
# Едно нещо(клас/метод) да е отговорно за едно единствено нещо
# не трябва да се преплита като функционалност за неща, които не би следвало класът да прави
# SRP - classes should have one responsibility

# Example - do not do like this
class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def register(self, student):
        pass

# The correct way - splitting the class

class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class StudentRecords:
    def get_student(self, id):
        pass

    def register(self, student):
        pass

# Open/Closed - Software entities like classes, modules, and functions should be open for extension but closed for modifications
# допълваме/разширява  някаква функционалност, не променяме
# Проверка: Ако се добави функционалност към вече съяествуващата функционалност след два месеца трябва ли аз да променям/добавям в същия клас, ако да,  то тогава вече правилото е на рушерно

# This can be achieved through:
# Abstraction
# Mix-ins
# Monkey-Patching
# Generic functions (using overloading)

# OCP violation (1)
# Let's imagine that we want to make a 40% discount of the semester taxes to all students with grades above 5
class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4

# Later we decide that we want to give a 20% discount to students with grades above 4
class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
	if self.average_grade > 5:
            return self.semester_tax * 0.4
	elif self.average_grade > 4:
	    return self.semester_tax * 0.2

# OCP Approaches
class StudentTaxes:
    def __init__(self, name, semester_tax, avg_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4

class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2

# Example:
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Wolf"

class Chicken(Animal):
    def make_sound(self):
        return "Peow"

class Pig(Animal):  # може да добавяме колкото искаме нови животни(класове) без да променяме функционалността (animal_sound, Animal)
    def make_sound(self):
        return "Gruh"

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken(), Pig()]
animal_sound(animals)


# Liskov Substitution - Derived types must be completely substitutable for their base types
# всичко(клас атрибути, instance атрибути, instance методи, клас методи, static методи) за base класа трябва да е валидно и за наследника

# класовете, които са наследници и имаме някакви инстанции от тях, по принцип трябва да бъдат заменяеми с техните base класовве
# принципите и методите, които имаме в base класа, трябва да са валидни и за child класа
# всеки един от методите в base класа трябва да бъде валиден и за наследниците
# всички методи за base класа трябва да са валидни и за наследниците и, че наследниците могат да доразширяват функционалността на base класа
# Derived classes
# only extend functionalities of the base class
# must not remove base class behavior
# Student IS-SUBSTITUTED-FOR Person

# LSP is fundamental to a good object-oriented software design because it emphasizes one of its core traits – polymorphism
# It is about creating correct hierarchies so that classes derived from a base one are polymorphic along the parent one
# Carefully thinking about new classes in the way that LSP suggests helps us to extend the hierarchy correctly
# We could say that LSP contributes to the OCP

# Design Smell – Violations
# If the code is checking the type of class
# Overridden methods change their behavior 
# Override a method of the superclass by an empty method
# Base class depends on its subtypes


# Interface Segregation
# A client should not depend on methods it does not use
# A good way of ensuring this is by separation through multiple inheritance
# Тhis is precisely the purpose of the mix-ins - to provide multiple clients with specific behaviours
# ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy

# ISP issues
# Python doesn't have interfaces
# Languages that do have interfaces:
# Breaking them up too much ends up with interfaces implementing interfaces

# ISP Violations
# Class Shape draws rectangle and circle
# Class Circle or Rectangle implementing the Shape class must define the methods draw_rectangle() and draw_circle()
class Shape:
    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError

# Class Rectangle implements the method draw_circle it has no use of
# Class Circle implements method draw_rectangle

class Rectangle(Shape):
    def draw_rectangle(self):
        pass
    def draw_circle(self):
        pass
class Circle(Shape):
    def draw_rectangle(self):
        pass
    def draw_circle(self):
        pass

# ISP Approaches
# To make Shape conform to the ISP principle, we segregate the actions into different classes
# Classes Circle and Rectangle can inherit from class Shape and implement their own draw behaviour

class Shape:
    def draw(self):
        raise NotImplementedError
class Rectangle(Shape):
    def draw(self):
        pass
class Circle(Shape):
    def draw(self):
        pass


# Dependency Inversion - бащиният клас не трябва да знае нищо за наследниците си
# Interesting design principle by which we protect our code by making it independent of things that are fragile, volatile, or out of our control
# Depend on abstractions, not on concretions
# High-level modules should not depend on low-level modules. Both should depend on abstractions

# !!! Abstractions should not depend on details. Details should depend on abstractions !!!


# Dependency Injection
# Software engineering technique for defining the dependencies among objects
# Why use Dependency Injection?
# Decreases coupling between a class and its dependency
# Can be applied to legacy code as a refactoring because it doesn’t require any change in code behaviour
# Allows a client to remove all knowledge of a concrete implementation that it needs to use
