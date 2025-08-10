
# library_system.py

class Book:
    """Base class representing a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Represents a digital book (inherits from Book)."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size  # in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Represents a printed book (inherits from Book)."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class that uses composition to manage books."""
    def __init__(self):
        self.books = []  # Holds Book, EBook, PrintBook instances

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
