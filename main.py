import argparse
import logging
# استدعي ملفك
import library

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="مشروع تالا الخاص")
    subparsers = parser.add_subparsers(dest="command")

    # أضيفي هنا الأوامر التي تريدينها فقط
    add_parser = subparsers.add_parser("add")

    args = parser.parse_args()

    # هنا اربطي أوامرك بالكود الذي ستكتبينه في library.py
    if args.command == "add":
        print("تالا ستقوم ببرمجة الإضافة هنا...")

if __name__ == "__main__":
    main()
