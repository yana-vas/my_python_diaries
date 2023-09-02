# Static Methods - It knows nothing about the class or instance it is called on
# It cannot modify object state or class state
# It could be put outside the class, but it is inside the class where it is applicable
# To turn a method into a static we add a line with @staticmethod in front of the method header

# Статични методи
#   -> няма достъп до self
#   -> нe знае и не трябва да знае нищо, което е свързано с класа
#   -> може да бъде дефинирано като отделна самостоятелна функция (намира се в класа, защото има някаква логика да е свързано/related с него
#   -> @staticmethod декоратор превръща метода в статичен (removes self)

class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):  # it does not take self parameter
        return age >= 18


print(Person.is_adult(5))   # False  (It is better to use the class, when calling static methods)
girl = Person("Amy")
print(girl.is_adult(20))     # True

# Class Methods - It is bound to the class and not the object of the class
# It can modify a class state that would apply across all the instances of the class
# To turn a method into a class method we add a line with @classmethod in front of the method header

# We generally use class method to create factory methods


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(['tomato sauce', 'parmesan', 'pepperoni'])

    @classmethod
    def quattro_formaggi(cls):
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])


first_pizza = Pizza.pepperoni()
second_pizza = Pizza.quattro_formaggi()


# Simply provide a shortcut for creating new instance objects
# Ensures correct instance creation of the derived class
# You could easily follow the Don't Repeat Yourself (DRY) principle using class methods

class Laptop:
    def __init__(self, memory, model):
        self.memory = memory
        self.model = model

    @classmethod
    def low_memory_laptop(cls):
        return cls(8, 'Asus')

    @classmethod
    def high_memory_laptop(cls, model):
        return cls(32, model)

    def __str__(self):
        return f"Laptop model is {self.model} with ram {self.memory}"


laptop_for_my_brother = Laptop.low_memory_laptop()
laptop_for_the_favorite_child_aka_me = Laptop.high_memory_laptop('HP')


# Overriding Using Class Methods
# A static method is a method that knows nothing about the class or instance it is called on
# A class method, on the other hand, is bound to the class and not the object of the class

# Overriding Using Methods
class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):
        if value < Person.min_age or \
           value > Person.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value
class Employee(Person):
    min_age = 16
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(value):
        if value < Employee.min_age or \
           value > Employee.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


# Overriding Using a Class Method

class Person:
   min_age = 0
   max_age = 150

   def __init__(self, name, age):
      self.name = name
      self.age = age

   @classmethod
   def __validate_age(cls, value):
      raise ValueError(f'{value} must be between '
                       f'{cls.min_age} and {cls.max_age}')
# __validate_age() takes the class attributes of class Person

   @property
   def age(self):
       return self.__age

   @age.setter
   def age(self, value):
       self.__validate_age(value)
       self.__age = value

class Employee(Person):
    min_age = 16
# __validate_age() takes the class attribute min_age of class Employee

    def __init__(self, name, age, salary):
        super().__init__(name, age) # when checking the age of the Employee
        self.salary = salary
