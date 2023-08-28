book = input()

book_sum = 0
current_book = input()
book_is_found = False
while current_book != "No More Books":
    if current_book == book:
        book_is_found = True
        break
    book_sum += 1
    current_book = input()
if book_is_found:
    print(f"You checked {book_sum} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_sum} books.")
    