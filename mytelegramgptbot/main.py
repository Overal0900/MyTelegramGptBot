import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler,
    filters, ContextTypes
)

from handlers.basic import start, menu_callback
from handlers.gpt import chat_with_gpt
from handlers import register_all_handlers

load_dotenv()
TOKEN = os.getenv("MYTG_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("awaiting_gpt"):
        await chat_with_gpt(update, context)
        context.user_data["awaiting_gpt"] = False
    else:
        await update.message.reply_text("Неизвестная команда. Нажмите /start.")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Базовые хендлеры
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

    # Регистрируем все остальные хендлеры
    register_all_handlers(app)

    # --- Добавляем обработчик для ответов викторины ---
    from handlers.quiz import handle_quiz_answer
    app.add_handler(CallbackQueryHandler(handle_quiz_answer, pattern=r'^quiz_answer:'))

    logger.info("✅ Бот успешно запущен.")
    app.run_polling()


if __name__ == "__main__":
    main()





