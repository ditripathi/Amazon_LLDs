/*
Main Classes
Book

Attributes: title, author, isbn, availability
Methods: check_out(), return_book()
Member

Attributes: member_id, name, borrowed_books
Methods: borrow_book(book), return_book(book)
Library

Attributes: books, members
Methods: add_book(book), remove_book(book), issue_book(book, member), return_book(book, member)
Librarian

Attributes: employee_id, name
Methods: add_book(book, library), remove_book(book, library), issue_book(book, member, library), return_book(book, member, library)
EBook (inherits Book)

Additional Attributes: file_size, format
PrintedBook (inherits Book)

Additional Attributes: pages, publisher
*/

// Base class for a book
abstract class Book {
    protected String title;
    protected String author;
    protected String isbn;
    protected boolean availability;

    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.availability = true;
    }

    public boolean checkOut() {
        if (availability) {
            availability = false;
            return true;
        }
        return false;
    }

    public void returnBook() {
        availability = true;
    }
}

class EBook extends Book {
    private double fileSize;
    private String format;

    public EBook(String title, String author, String isbn, double fileSize, String format) {
        super(title, author, isbn);
        this.fileSize = fileSize;
        this.format = format;
    }
}

class PrintedBook extends Book {
    private int pages;
    private String publisher;

    public PrintedBook(String title, String author, String isbn, int pages, String publisher) {
        super(title, author, isbn);
        this.pages = pages;
        this.publisher = publisher;
    }
}

class Member {
    private int memberId;
    private String name;
    private List<Book> borrowedBooks;

    public Member(int memberId, String name) {
        this.memberId = memberId;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }

    public boolean borrowBook(Book book) {
        if (book.checkOut()) {
            borrowedBooks.add(book);
            return true;
        }
        return false;
    }

    public boolean returnBook(Book book) {
        if (borrowedBooks.contains(book)) {
            book.returnBook();
            borrowedBooks.remove(book);
            return true;
        }
        return false;
    }
}

class Library {
    private List<Book> books;
    private List<Member> members;

    public Library() {
        this.books = new ArrayList<>();
        this.members = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void removeBook(Book book) {
        books.remove(book);
    }

    public boolean issueBook(Book book, Member member) {
        return member.borrowBook(book);
    }

    public boolean returnBook(Book book, Member member) {
        return member.returnBook(book);
    }
}

class Librarian {
    private int employeeId;
    private String name;

    public Librarian(int employeeId, String name) {
        this.employeeId = employeeId;
        this.name = name;
    }

    public void addBook(Book book, Library library) {
        library.addBook(book);
    }

    public void removeBook(Book book, Library library) {
        library.removeBook(book);
    }

    public boolean issueBook(Book book, Member member, Library library) {
        return library.issueBook(book, member);
    }

    public boolean returnBook(Book book, Member member, Library library) {
        return library.returnBook(book, member);
    }
}

// Example Usage
public class LibraryManagementSystem {
    public static void main(String[] args) {
        Library library = new Library();
        Librarian librarian = new Librarian(1, "John Doe");

        PrintedBook book1 = new PrintedBook("1984", "George Orwell", "1234567890", 328, "Secker & Warburg");
        EBook ebook1 = new EBook("Digital Fortress", "Dan Brown", "0987654321", 2.5, "PDF");

        Member member = new Member(1, "Alice");

        librarian.addBook(book1, library);
        librarian.addBook(ebook1, library);

        // Issue a book to a member
        librarian.issueBook(book1, member, library);

        // Return the book
        librarian.returnBook(book1, member, library);
    }
}
