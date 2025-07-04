class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year"""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Print deletion message when book is deleted"""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """Return user-friendly string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Return official string representation that can recreate the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"