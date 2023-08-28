from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for r in range(len(self.photos)):
            page = self.photos[r]

            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                # self.photos[r+1].append(label)
                return f"{label} photo added successfully on page {r+1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        photos = []
        for page in self.photos:
            photos.append(' '.join(['[]' for el in page]))

        return f'-----------\n' + f'\n-----------\n'.join(photos) + f'\n-----------'


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
