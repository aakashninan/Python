"""Program to Model Library–Book Relationship with Composition and Aggregation@AakashNinan IMCA Rollno:02"""
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  

    def add_book(self, title):  # Composition
        book = Book(title)
        self.books.append(book)

    def add_existing_book(self, book):  # Aggregation
        self.books.append(book)

    def show_books(self):
        print(f"Books in {self.name}:")
        for b in self.books:
            print("-", b.title)

lib = Library("City Library")
lib.add_book("Python Basics")
lib.add_book("Data Structures")

b1 = Book("Artificial Intelligence")
lib.add_existing_book(b1)

lib.show_books()
