# Inheritance - extend the functionality of the code's existing classes to eliminate repetitive code
# Inheritance is the capability of one class to inherit the methods and properties from another class
# super() - returns a temporary object of the superclass; Allows you to call methods of the superclass in your subclass
# extend the functionality of the inherited method

# Tip: mark directory as source root, so you can import easily

# Single inheritance => When a child class inherits properties from a single parent class only
class Person:  # бащин клас (майчин)
    def __init__(self, name, age):
        self.name = name
        self.age = age


# наследника зане за класа, който е наследил, но класа, който е бил наследен няма представа за наследника
# Employee може да ползва атрибутите, методите и всичко от Person, но Person не може да ползва нищо от Employee
# наследяваме, само когато дъщерният клас ползва всички атрибути и всички методи от бащиният клас
class Employee(Person):  # наследява атрибутите от Person -> дъщерен клас
    def __init__(self, name, age, work_id, salary):
        super().__init__(name, age)  # наследява атрибутите от Person (първо ще получим name и после age)
        # super() -> реферира към първия наследен клас
        # super().__init__(age=age, name=name)  # първо ще получим age и после name

        self.work_id = work_id
        self.salary = salary


employee = Employee('Yana', 15, 1254, 1000)
print(employee.name)

# Multiple Inheritance => When a child inherits from more than one parent class
# (When a child class becomes a parent class for another child class)
class Father:
    def __init__(self):
        self.father_name = "Tayler Evans"

    def say_name(self):
        return self.father_name

class Mother:
    def __init__(self):
        self.mother_name = 'Emma Watson'

    def say_name(self):
        return self.mother_name


class Daughter(Father, Mother):  # търсим в реда, по който са дефинирани класовете ни
    def __init__(self):
        Father.__init__(self)  # super().__init__()
        # super() -> реферира към първия наследен клас
        Mother.__init__(self)


d = Daughter()
print(d.say_name())


# Hierarchical Inheritance - When more than one child classes are created from a single parent class
class Parent:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return f'Hi! I am {self.name}'


class Daughter(Parent):
    def __init__(self, name):
        super().__init__(name)

    def relation(self):
        return "I am my parent's daughter"


class Son(Parent):
    def __init__(self, name):
        super().__init__(name)

    def realtion(self):
        return "I am parent's son"


# Mixin - малки класове, само с методи, с малка функционалност и може да се наследи от други сласове (когато се наследяват mixin се записват последни)
# ▪ A mixin is a class that is implementing a specific set of features that is needed in many different classes
# ▪ A mixin is a class which has no data, only methods
# ▪ Mixins cannot be instantiated by themselves
# ▪ We use mixins to extend functionality

# Exampple:

class RadioMixin():
    def play_song_on_station(self, station_frequency):
        return f"playing song on radio frequency {station_frequency}"


class Vehicle:
    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        pass


class Car(Vehicle, RadioMixin):
    pass


class Clock(RadioMixin):
    pass


# Inheritance - extend the functionality of the code's existing classes to eliminate repetitive code
# Encapsulation - stop objects from interacting with each other so classes cannot change or interact with the specific variables and functions of an object
# Abstraction - isolate the impact of changes made to the code so the change will only affect the variables shown and not the outside code
# Polymorphism - allows different classes to have methods with the same name