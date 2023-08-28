from project.person import Person


class Child(Person):
    def __init__(self, name, age):
        super(Child, self).__init__(name, age)
