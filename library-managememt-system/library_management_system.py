class Library:
    def __init__(self, list_of_books, library_name):
        # creating a blank dictionary
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = library_name

        # add book to dictionary
        for books in self.list_of_books:
            self.lend_data[books] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}){books}")

    def lend_book(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = author
            else:
                print(f"Sorry This book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def add_books(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def return_books(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("This book is already lended")
        else:
            print("Sorry can't find the book")


def main():
    list_books = ['Python', 'Linux', 'Go', 'javascript', 'django']
    library_name = 'Programming'

    programming = Library(list_books, library_name)

    print(f"Welcome to {programming.library_name} library \n \n 'q' for exit \n 'd' for display books \n 'a' to add "
          f"book \n "
          f"'l' for lend book \n 'r' for return book \n")
    print('------------------------')

    exit_system = False
    while exit_system is not True:
        _input = input(" Enter option : ")
        print("\n")

        if _input == "q":
            exit_system = True

        elif _input == "d":
            programming.display_books()

        elif _input == "a":
            _addbook = input("Book Name : ")
            programming.add_books(_addbook)

        elif _input == "l":
            _name = input("Name : ")
            _bookname = input("Book Name : ")
            print("\n Book Lend \n")
            programming.lend_book(_bookname, _name)

        elif _input == "r":
            _name = input("Name : ")
            _bookname = input("Book Name : ")
            programming.return_books(_bookname, _name)


if __name__ == '__main__':
    main()
