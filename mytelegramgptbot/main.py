import logging
import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes
)

from handlers.basic import start, menu_callback
from handlers.gpt import chat_with_gpt

load_dotenv()
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("MYTG_BOT_TOKEN")


async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("awaiting_gpt"):
        await chat_with_gpt(update, context)
        context.user_data["awaiting_gpt"] = False
    else:
        await update.message.reply_text("Неизвестная команда. Нажмите /start.")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()




