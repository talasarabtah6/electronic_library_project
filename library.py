import logging

# قائمة لتخزين الكتب مؤقتاً
books = []

def add_book(title):
    if title:
        books.append(title)
        logging.info(f"Book '{title}' added to the library.")
        return True
    return False

def search_books(query):
    """دالة البحث عن كتاب - مهمة تالا LIB-002"""
    all_books = list_books()
    results = [b for b in all_books if query.lower() in b.lower()]
    return results

def list_books():
    return books
