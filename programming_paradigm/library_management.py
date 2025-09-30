# library_management.py

class Book:
    def __init__(self, title, author):
        """
        Initialize a Book with a title, author, and an internal
        flag _is_checked_out to track if it’s lent out.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Mark the book as checked out if it isn’t already.
        Returns True on success, False if the book was already lent.
        """
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """
        Mark the book as returned if it was checked out.
        Returns True on success, False if it wasn’t checked out.
        """
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """
        Check whether the book is currently available.
        Returns True if not checked out, False otherwise.
        """
        return not self._is_checked_out


class Library:
    def __init__(self):
        """
        Initialize a Library with a private list _books
        to hold Book instances.
        """
        self._books = []

    def add_book(self, book):
        """
        Add a Book instance to the library’s collection.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Find a book by title and attempt to check it out.
        Returns True if checked out successfully, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        """
        Find a book by title and attempt to return it.
        Returns True if returned successfully, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        """
        Print all books that are not currently checked out.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
