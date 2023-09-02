class Room:

    def __init__(self, n: int, c: int):
        self.number = n
        self.capacity = c
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if self.is_taken is False and self.capacity >= people:
            self.is_taken = True
            self.guests = people
            return
        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
            return
        return f"Room number {self.number} is not taken"
