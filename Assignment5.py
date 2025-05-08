# Question 1: Creating a class called Book

# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.__pages = pages   # Encapsulated (private) attribute
        self.current_page = 1

    def read(self):
        print(f"Reading '{self.title}' by {self.author} 📖.")

    def get_pages(self):
        return self.__pages

# Subclass with polymorphism
class EBook(Book):
    def __init__(self, title, author, pages, file_format):
        super().__init__(title, author, pages)
        self.file_format = file_format

    # Polymorphism: overrides read() method
    def read(self):
        print(f"Reading digital book '{self.title}' in {self.file_format} format👩🏽‍💻.")

# Example usage
book1 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 200)
ebook1 = EBook("Atomic Habits", "James Clear", 250, "PDF")

book1.read()
ebook1.read()

print("Pages in book1:", book1.get_pages())
print("Pages in ebook1:", ebook1.get_pages())


# Polymorphism Challenge/ Question 2 
class Car:
    def move(self):
        return "The car is moving🚘."
class flight:
    def move(self):
        return "The flight is flying✈️."
class Boat:
    def move(self):
        return "The boat is sailing🚤."
   
    # polymorphism in action 
for vehicle in [Car(), flight(), Boat()]:
    print(vehicle.move())
