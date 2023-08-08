from main import books


def print_best_books():
    best_books = sorted(books, key=lambda x: (x.rating*-1, x.price))[:10]
    for book in best_books:
        print(book)


book = (x for x in books)


def print_next_availableBook():
    print(next(book))


user_validations = {
    '1': print_best_books,
    '2': print_next_availableBook
}


def menu():
    user_input = None
    while user_input != 'q':
        print("1) Show Best 10 Books.")
        print("2) Show Next Available Book.")
        print("q) Exit")
        user_input = input("Enter Option : ")
        if user_input in ('1', '2'):
            user_validations[user_input]()


menu()
