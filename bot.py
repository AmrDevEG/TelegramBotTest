# استيراد المكتبات اللازمة
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- توكن البوت الخاص بك ---
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not BOT_TOKEN:
    # هذا الكود سيوقف البوت لو لم يجد التوكن، وهذا أفضل من أن يعمل بخطأ
    raise ValueError("خطأ: لم يتم العثور على متغير البيئة TELEGRAM_TOKEN. يرجى إضافته.")
# -----------------------------

# تعريف وظيفة الأمر /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! جرب أن تسألني (عامل ايه؟)")

# تعريف وظيفة الأمر /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("الأوامر المتاحة:\n/start - لبدء المحادثة\n/channel - للحصول على رابط قناتي")

# وظيفة الأمر /channel
async def channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تفضل، هذه هي قناتي على تيليجرام: https://t.me/Amr_x64")

# ⭐⭐ الدالة الجديدة للردود الذكية ⭐⭐
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower().strip()
    print(f"User said: {user_text}")

    if 'عامل ايه' in user_text or 'ازيك' in user_text:
        response = "الحمدلله بخير، شكراً لسؤالك!"
    elif 'السلام عليكم' in user_text:
        response = "وعليكم السلام ورحمة الله وبركاته."
    elif 'صباح الخير' in user_text:
        response = "صباح النور والسرور!"
    elif 'مساء الخير' in user_text:
        response = "مساء الفل عليك."
    else:
        response = "لم أفهم ما تقصده. يمكنك استخدام الأوامر مثل /start أو /channel."
    
    await update.message.reply_text(response)


# تعريف وظيفة للتعامل مع الأخطاء
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

# الكود الرئيسي لتشغيل البوت
if __name__ == '__main__':
    print("البوت قيد التشغيل...")
    app = Application.builder().token(TOKEN).build()

    # إضافة الأوامر
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('channel', channel_command)) 

    # إضافة معالج للرسائل النصية العادية (هنا نستخدم الدالة الجديدة)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # إضافة معالج للأخطاء
    app.add_error_handler(error)

    print("البوت ينتظر الرسائل...")
    app.run_polling()
