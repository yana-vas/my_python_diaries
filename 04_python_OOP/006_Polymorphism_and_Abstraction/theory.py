

# Polymorphism - на различни видове обекти, които имат един и общи корен(метод), но различни форми(функции). Имаме възможността да извикваме един и същи метод, върху различни инстанции

class Shape:
     def calculate_area(self):
         return None


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    def __init__(self, side_length, height):
        self.side_length = side_length
        self.height = height

    def calculate_area(self):
        return (self.side_length*self.height)/2

# with POLYMORPHISM
shapes = [Square(3), Triangle(6, 3)]
for shape in shapes:
    print(shape.calculate_area())

# WITHOUT polymorphism
shapes = [Square(3), Triangle(6, 3)]
for shape in shapes:
    if isinstance(shape, Square):
        area = shape.calculate_square_area()
    if isinstance(shape, Triangle):
        area = shape.calculate_triangle_area()
    print(area)


# Abstractions
# От абстрактните класове не могат да се правят инстанции

# За да създадем абстрактен клас трябва да наследим от ABC и да има поне един абстрактен метод (from abs import ABC, abstractmethond)
# Абстрактните методи трябва да се пренаписват в наследника (дъщерните класове)
# От абстрактните класове не могат да се правят инстанции


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return "Shape"

class Square(Shape):
    def calculate_area(self):
        return "......."


# Duck Typing
# Duck Typing is a type system used in dynamic languages
# "If it looks like a duck and quacks like a duck, it's a duck"
# i.e., we don't care about objects' types, but whether they have the methods we need

class Cat:
    def sound(self):
        print("Meow!")

class Train:
    def sound(self):
        print("Sound from wheels slipping!")

for any_type in Cat(), Train():
    any_type.sound()


# Inheritance -всички атрибути и методи трябва да са валидни за наследника
# Encapsulation - да крием ранзи неяа, но и да ги валидираме
# Polymorphism - да имаме метод с едно и също име, но да иамаме същият метод с име и в наследниците
# Abstraction - Polymorphism + трябва да наследиме ABC класа и поне един абстрактен метод


# Abstract class
# да не се правят инстанции от него
# да служи като шаблон за неговите наследници, за да може да задължава задължително да се имплементират някакви методи
# наследява ABC и има поне един абстрактен метод

# Ако имаме полиморфизъм е препорачително да имаме абстрактен клас, обаче ако имаме наследяване не е задължително

# Полиморфизъм
# Във всички наследници трябва да има метод, който се казва по един и същи начин
# Едно и също име на метод, което има разлчни имплементации в наследниците
# Целта е, когато се итерира през различни обекти от един и същи тип (с общ наследник) да се гарантира, че ще има такъв метод, който да има различни имплементации



# Polymorphism is based on the Greek words "poly" (many) and "morphism" (forms)
# It is the ability to present the same interface for differing underlying forms though the interface of their base class
# e. g., Square and Triangle inherit Shape, so their instances can be used from an instance of type Shape

# A subclass can override a method of its superclass
# e. g., both triangle and square are shapes and have area

class Shape:
    def calculate_area(self):
        return None

class Square(Shape):
    side_length = 2
    def calculate_area(self):
        return self.side_length * 2

class Triangle(Shape):
    base_length = 4
    height = 3
    def calculate_area(self):
        return 0.5 * self.base_length * self.height


# Without Polymorphism - >A type check may be required before performing an action on an object to determine the correct method to call
for obj in Square(), Triangle():
    if isinstance(obj, Square):
        area = obj.calculate_square_area()
    elif isinstance(obj, Triangle):
        area = obj.calculate_triangle_area()
    print(area)


# Complile-Time Polymorphism
# Python does not support compile-time polymorphism or method overloading
# If a class has multiple methods with the same name, the method defined in the last will override the earlier one
class Person:
    def say_hello():
        return "Hi!"
    def say_hello():
        return "Hello"

print(Person.say_hello()) # Hello


# Overloading Built-in Methods
# Change the behavior of functions such as len, abs, str, repr, and so on
# To do this, you only need to define the corresponding special method in your class
class MyClass:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __len__(self):
        return self.size

my_class = MyClass("Class Name", 3)
print(len(my_class)) # 3


# Operator Overloading
# An operator behaves differently based on the type of the operands
# e.g., operator "+" is used to add two integers as well as join two strings and merge two lists
# It is overloaded by int class, str class and list class
integer = 1 + 1
string = "Hello, " + "SoftUni"
list = ["1", "2"] + ["3", "4"]

# Operator Magic Methods

#   __add__(self, other) => +
#   __sub__(self, other) => -
#   __mul__(self, other) => *
#   __floordiv__(self, other) => //
#   __truediv__(self, other) => /
#   __pow__(self, other) => **


# "Rich Comparison" Magic Methods
#   __lt__(self, other) => <
#   __le__(self, other) => <=
#   __eq__(self, other) => ==
#   __ne__(self, other) => !=
#   __gt__(self, other) => >
#   __ge__(self, other) => >=



class Purchase:
    def __init__(self, product_name, cost):
        self.product_name = product_name
        self.cost = cost

    def __add__(self, other):
        name = f'{self.product_name}, {other.product_name}'
        cost = self.cost + other.cost
        return Purchase(name, cost)

first_purchase = Purchase('sofa', 650)
second_purchase = Purchase('table', 150)
print(first_purchase + second_purchase)  # sofa, table; 800

class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

person_one = Person('John', 20)
person_two = Person('Natasha', 36)
print(person_one > person_two)  # False


# Duck Typing - a type system used in dynamic languages
# "If it looks like a duck and quacks like a duck, it's a duck"
# i.e., we don't care about objects' types, but whether they have the methods we need

# We can create a method that calls the sound method, no matter of what the object which makes the sound is
class Cat:
    def sound(self):
        print("Meow!")

class Train:
    def sound(self):
        print("Sound from wheels slipping!")

for any_type in Cat(), Train():
    any_type.sound()


# Abstraction -> hide all but the relevant data about an object to reduce complexity and increase efficiency
# In object-oriented programming, abstraction is one of the four central principles
# Abstraction can be achieved by:
#   - Functions and methods
#   - Abstract classes


# Abstract Classes - classes that contain one or more abstract methods
# An abstract method is a method that is declared, but contains no implementation
# Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods

# It could be achieved using exceptions, but it not a good practice
class Shape:
    def __init__(self):
        if type(self) is Shape:
            raise Exception('This is an abstract class')

    def area(self):
        raise Exception('This is an abstract class')

    def perimeter(self):
        raise Exception('This is an abstract class')

# Abstract base classes (ABCs) enforce derived classes to implement particular methods from the base class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self):
        raise NotImplementedError("Subclass must implement")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Meow!")

cat = Cat("Willy")
cat.sound()
dog = Dog("Willy")
dog.sound()
animal = Animal("Willy")
animal.sound()
# Meow!
# Bark!
# Error!


# Summary:
# Polymorphism means same function name being uses for different types
# Through abstraction, we hide all but the relevant data about an object
# Abstract classes may not be instantiated, and  require subclasses

