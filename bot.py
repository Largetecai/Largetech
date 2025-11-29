import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Read token from Render environment variable

async def start(update, context):
    await update.message.reply_text("🔥 Your bot is LIVE on Render!")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

def main():
    if not TOKEN:
        raise ValueError("❌ TELEGRAM_TOKEN not found! Add it in Render Environment Variables.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()