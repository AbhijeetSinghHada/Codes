class BookShelf:
    def __init__(self, *books):
        self.books = books

    def show_all_books(self):
        for book in self.books:
            print(book)

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


if __name__ == "__main__":
    book = Book("Harry Potter")
    book2 = Book("Python 101")
    shelf = BookShelf(book, book2)
    print(shelf)
    shelf.show_all_books()
