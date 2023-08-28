class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        # if not isinstance(other, Cat):
        #     raise ValueError(f"Operand cannot be applied between of instance of type Cat and instance of type {other.__class__.__name__}")
        if self.name == other.name and self.age == other.age:
            return True
        return False

    # def __len__(self):
    #     return self.age * 7


class MiniCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat_1 = Cat('Maci', 3)
cat_2 = Cat('Popi', 6)
print(cat_1 <= cat_2)
print(cat_1 == cat_2)


class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


person_1 = Person('BaSingSe', 20)
person_2 = Person('SiNing', 36)
print(person_1 > person_2)
