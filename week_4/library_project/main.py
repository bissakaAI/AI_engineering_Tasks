from student_data import data
from utils import helpers
from services import library

#add some books
data.add_book("python basics","john doe")
data.add_book("phyics", "joshua kim")


#display books 
print("library Collection: ")
for i in data.get_books():
    print(helpers.format_book(i))

# Borrow a book
print("\nBorrowing a book:")
print(library.borrow_book("Python Basics"))
