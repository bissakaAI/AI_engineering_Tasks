import student_data.data as data
def borrow_book(title):
    for book in data.get_books():
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            return f"you have borrowed '{book["title"]}'"
    return "book not available"