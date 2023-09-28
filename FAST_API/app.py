from fastapi import FastAPI
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
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_name}")
async def read_book(book_name):
    for book in BOOKS:
        if book.get('title').casefold() == book_name.casefold():
            return book
