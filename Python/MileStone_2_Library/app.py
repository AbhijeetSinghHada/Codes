from utils import Database


def Menu():
    print(
        """\n\nWelcome to Books Store\n*********************************************************\n
Enter the Option Number Below : 
1. To Add Book
2. List All the Books
3. Mark Book as Read
4. Delete Book
5. List All Unread Books
6. Search Book By Name
q. Quit
""")


user_choice = None


def prompt_add_book():
    name = input("Enter the Name of the Book : ")
    author = input("Enter the Author of the Book : ")

    val = Database.add_book(name, author)
    if val == True:
        print("Book Added Successfully.")
    else:
        print("Enter Book Name and Author Correctly.")


def prompt_delete_book():
    name = input("Enter the Name of the Book To Delete : ")
    Database.delete_book(name)


def prompt_mark_book_as_read():
    name = input("Enter the Name of the Book To mark Read : ")
    Database.mark_book_as_read(name)


def prompt_SearchName():
    name = input("Enter the Name of the Book To Search : ")
    Database.SearchBookByName(name)


if __name__ == "__main__":
    while (user_choice != 'q'):
        Menu()
        choices = {
            '1': prompt_add_book,
            '2': Database.list_books,
            '3': prompt_mark_book_as_read,
            '4': prompt_delete_book,
            '5': Database.list_undread_books,
            '6': prompt_SearchName
        }
        user_choice = input("Enter Option : ")
        print()
        # try:
        if user_choice in choices:
            choices[user_choice]()
        # except:
        #     print("There Has been a mistake. Please try again entering correct data.")
    print("Thank You For Visiting")
    print("Books Store By Abhi")
