class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("Roar", "Lady Gaga", "I won'visible_trees give up, no oh-oh-oh")
print(song.print_info())
print(song.play())
