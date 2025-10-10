# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        #Constructor to initialize the book details
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        #Destructor that runs when the object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        #Human-readable string representation
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        #Official representation used for recreating the object
        return f"Book('{self.title}', '{self.author}', {self.year})"


