from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplementedError



class Rectangle(Shape):
    def draw(self):
        pass

class Circle(Shape):
    def draw_rectangle(self):
        pass
    def draw_circle(self):
        pass


class Shape:
    def draw(self):
        raise NotImplementedError
class Rectangle(Shape):
    def draw(self):
        pass
class Circle(Shape):
    def draw(self):
        pass
