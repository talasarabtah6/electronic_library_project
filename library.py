import logging

# قائمة لتخزين الكتب مؤقتاً
books = []

def add_book(title):
    if title:
        books.append(title)
        logging.info(f"Book '{title}' added to the library.")
        return True
    return False

def list_books():
    return books
