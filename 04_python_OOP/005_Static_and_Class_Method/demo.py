# import math
#
#
# class Points:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def calculate_distance(self, point):
#         return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
#
#     @staticmethod
#     def calc_distance(point_1, point_2):
#         return math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
#
# print(Person.is_adult(5))  #False
# girl = Person("Amy")
# print(girl.is_adult(20))  #True


# class Calculator:
#
#     @staticmethod
#     def add(*args):
#         result = 0
#         for n in args:
#             result += n
#         return result
#
#     @staticmethod
#     def multiply(*args):
#         result = 1
#         for n in args:
#             result *= n
#         return result
#
#     @staticmethod
#     def divide(*args):
#         result = args[0]
#         for i in range(1, len(args)):
#             result /= args[i]
#         return result
#
#     @staticmethod
#     def subtract(*args):
#         result = args[0]
#         for i in range(1, len(args)):
#             result -= args[i]
#         return result
#


# 2 - Shop

class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    
