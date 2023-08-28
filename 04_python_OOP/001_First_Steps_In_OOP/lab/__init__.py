import random


class Snake:
    def __init__(self, specie, color, size, price, age):
        self.specie = specie
        self.color = color
        self.size = size
        self.price = price
        self.age = age

    def eating(self):
        food = ["mouses", "another snake", "you", "eggs", "insects"]
        curr_food = random.choice(food)
        return f"Please, don't disturb the snake. It's eating {curr_food} at the moment"

    def sleeping(self):
        return "Sleeping..."

    def biting(self):
        return "Call the ambulance!!! You are bleeding."


python = Snake("python", "green", 2, 2000, 1)
print(python.eating())