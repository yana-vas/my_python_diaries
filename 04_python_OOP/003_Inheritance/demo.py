class RadioMixin():
    def play_song_on_station(self, station_frequency):
        return f"playing song on radio frequency {station_frequency}"


class Vehicle:
    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        pass


class Car(Vehicle, RadioMixin):
    pass


class Clock(RadioMixin):
    pass
