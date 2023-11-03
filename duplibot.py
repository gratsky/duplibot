import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context):
    """Отправляет сообщение на команду /start."""
    await update.message.reply_text(
        "Привет! Отправь мне сообщение, а я его дублирую 😏😏"
    )


async def duplicate_message(update: Update, context):
    """Дублирует отправленное сообщение."""
    await update.message.reply_text(update.message.text)


def main():
    """Запускает бота."""
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, duplicate_message))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()