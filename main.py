import argparse
import logging
from library import add_book, list_books

# إعداد التسجيل (Logging)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Electronic Library System")
    parser.add_argument('--add', help="Add a new book title")
    parser.add_argument('--list', action='store_true', help="List all books")

    args = parser.parse_args()

    if args.add:
        if add_book(args.add):
            print(f"Success: {args.add} has been added.")
    elif args.list:
        all_books = list_books()
        print(f"Library Content: {all_books}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
