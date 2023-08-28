class Circle:
    pi = 3.14

    def __init__(self, r):
        self.radius = r

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = Circle.pi * self.radius*self.radius
        return float(f"{area:.2f}")

    def get_circumference(self):
        circumference = 2*Circle.pi*self.radius
        return circumference


circle = Circle(10)
circle.set_radius(12)
print(type(circle.get_area()))
print(circle.get_circumference())

