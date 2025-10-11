class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        
class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
        
class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []
    
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        return self.books
