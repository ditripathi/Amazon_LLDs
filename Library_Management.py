'''
Main Classes


--> Book
Attributes: title, author, isbn, availability
Methods: check_out(), return_book()


--> Member 
Attributes: member_id, name, borrowed_books
Methods: borrow_book(book), return_book(book)

-- Library
Attributes: books, members
Methods: add_book(book), remove_book(book), issue_book(book, member), return_book(book, member)

-- Librarian
Attributes: employee_id, name
Methods: add_book(book, library), remove_book(book, library), issue_book(book, member, library), return_book(book, member, library)

-- EBook (inherits Book)
Additional Attributes: file_size, format

-- PrintedBook (inherits Book)
Additional Attributes: pages, publisher

'''


# Base class for a book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = True

    def check_out(self):
        if self.availability:
            self.availability = False
            return True
        return False

    def return_book(self):
        self.availability = True

class EBook(Book):
    def __init__(self, title, author, isbn, file_size, format):
        super().__init__(title, author, isbn)
        self.file_size = file_size
        self.format = format

class PrintedBook(Book):
    def __init__(self, title, author, isbn, pages, publisher):
        super().__init__(title, author, isbn)
        self.pages = pages
        self.publisher = publisher

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.check_out():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def issue_book(self, book, member):
        if member.borrow_book(book):
            return True
        return False

    def return_book(self, book, member):
        if member.return_book(book):
            return True
        return False

class Librarian:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def add_book(self, book, library):
        library.add_book(book)

    def remove_book(self, book, library):
        library.remove_book(book)

    def issue_book(self, book, member, library):
        return library.issue_book(book, member)

    def return_book(self, book, member, library):
        return library.return
