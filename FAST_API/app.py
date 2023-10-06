from fastapi import Body, FastAPI
app = FastAPI()

BOOKS = [
    {'title': 'Harry Potter', 'author': 'J. K. Rowling', 'category': 'Fantasy'},
    {'title': 'Jurassic Park', 'author': 'Michael Crichton',
        'category': 'Science Fiction'},
    {'title': 'The Martian', 'author': 'Andy Weir', 'category': 'Science Fiction'},
    {'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'category': 'Thriller'},
    {'title': 'The Fellowship of the Ring',
        'author': 'J. R. R. Tolkien', 'category': 'Fantasy'},
    {'title': 'A Game of Thrones',
        'author': 'George R. R. Martin', 'category': 'Fantasy'},
    {'title': 'A Clash of Kings', 'author': 'George R. R. Martin', 'category': 'Fantasy'},
    {'title': 'A Storm of Swords', 'author': 'George R. R. Martin',  'category': 'Drama'},
    {'title': 'A Feast for Crows',
        'author': 'George R. R. Martin',  'category': 'Thriller'},

]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/my_book")
async def my_favorite_book():
    return BOOKS[5]


@app.get("/books/{book_name}")
async def read_book(book_name: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_name.casefold():
            return book


@app.get("/books/")
async def get_books_by_category(category: str):
    book_list = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            book_list.append(book)
    return book_list


@app.get("/books/byauthor/{author}/")
async def get_books_by_author(author, category=None):
    book_list = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            if category:
                if book.get("category").casefold() == category.casefold():
                    book_list.append(book)
                continue
            book_list.append(book)
    return book_list


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(new_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == new_book.get("title").casefold():
            BOOKS[i] = new_book


@app.delete("/books/delete_book/{book_name}")
async def delete_books(book_name: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_name.casefold():
            BOOKS.pop(i)
