from project.user import User


class Library:

    def __init__(self):
        self.user_records = []  # store the users (users objects) of the library
        self.books_available = {}  # keep information regarding the authors (key: str) and the books available for
        # each of the authors (list of strings)
        self.rented_books = {}  # usernames (key: str) and nested dictionary as a value in which will keep
        # information regarding the book names (key: str) and days left before returning the book to the library (
        # int) - ({usernames: {book names: days to return}})

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author] and book_name not in user.books:
            user.books.append(book_name)
            self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            self.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        return f"The book \"{book_name}\" is already rented and will be available in {self.rented_books[user.username][book_name]} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            self.rented_books[user.username] = {}
            user.books.remove(book_name)
        return f"{user.username} doesn't have this book in his/her records!"
