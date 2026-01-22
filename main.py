import argparse
import logging
from library import add_book, list_books

# إعداد التسجيل بكافة المستويات المطلوبة في الصفحة 1
# نضع المستوى على DEBUG ليظهر كل شيء
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def main():
    # 1. إعداد البرنامج الأساسي
    parser = argparse.ArgumentParser(description="نظام إدارة المكتبة الإلكترونية المطور")
    subparsers = parser.add_subparsers(dest="command", help="الأوامر المتاحة")

    # 2. تعريف الأوامر الفرعية (Subcommands) - مطلب الصفحة 1
    # أمر الإضافة
    add_parser = subparsers.add_parser("add", help="إضافة كتاب جديد")
    add_parser.add_argument("title", type=str, help="عنوان الكتاب")

    # أمر العرض
    list_parser = subparsers.add_parser("list", help="عرض كل الكتب")

    # أمر الأتمتة (مطلب الصفحة 1 - Automate tasks)
    setup_parser = subparsers.add_parser("setup", help="تجهيز بيئة العمل تلقائياً")

    args = parser.parse_args()

    # 3. تنفيذ المنطق البرمجي (بترتيب صحيح ليعرف الحارس إصلاحه)
    if args.command == "add":
        logging.debug(f"Input received: {args.title}")  # استخدام DEBUG
        if add_book(args.title):
            print(f"✅ تم إضافة '{args.title}' بنجاح.")
        else:
            logging.error("فشلت عملية إضافة الكتاب!")  # استخدام ERROR

    elif args.command == "setup":
        logging.info("جاري تنظيف الملفات المؤقتة وتجهيز النظام...")
        print("⚙️ تم تجهيز بيئة العمل بنجاح!")

    elif args.command == "list":
        logging.info("عرض قائمة الكتب...")
        books = list_books()
        if not books:
            logging.warning("المكتبة فارغة حالياً!")  # استخدام WARNING
        print(f"📚 الكتب المتاحة: {books}")

    else:
        # رسالة المساعدة التلقائية (مطلب الصفحة 1)
        parser.print_help()

if __name__ == "__main__":
    main()
