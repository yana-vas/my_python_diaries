# ----------------- problem 1 ------------------

# class Robot:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def sensors_amount():
#         return 1
#
#
# class MedicalRobot(Robot):
#     @staticmethod
#     def sensors_amount():
#         return 6
#
#
# class ChefRobot(Robot):
#     @staticmethod
#     def sensors_amount():
#         return 4
#
#
# class WarRobot(Robot):
#     @staticmethod
#     def sensors_amount():
#         return 12
#
# basic_robot = Robot('Robo')
# da_vinci = MedicalRobot('Da Vinci')
# moley = ChefRobot('Moley')
# griffin = WarRobot('Griffin')
#
# print(basic_robot.sensors_amount())
# print(da_vinci.sensors_amount())
# print(moley.sensors_amount())
# print(griffin.sensors_amount())


# ----------------- problem 2 ------------------

class ImageArea:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()
