import sys
import re

# جلب رسالة الـ Commit التي كتبها المستخدم
commit_msg_filepath = sys.argv[1]
with open(commit_msg_filepath, 'r') as f:
    message = f.read()

# الصيغة المطلوبة: نوع(رقم التذكرة): وصف
# مثال: feat(LIB-001): add something
pattern = r'^(feat|fix|docs|refactor|test)\(LIB-\d+\): .+'

if not re.match(pattern, message):
    print("-" * 50)
    print("❌ خطأ في صيغة الـ Commit!")
    print("يجب أن تكون الصيغة: type(LIB-XXX): description")
    print("أمثلة مقبولة: feat(LIB-001): add login")
    print("-" * 50)
    sys.exit(1) # هذا الرقم يخبر جيت أن يرفض الحفظ
