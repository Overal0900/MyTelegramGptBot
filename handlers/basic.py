"""Хендлеры базового меню."""
import logging
import asyncio
from pathlib import Path
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляем главное меню с изображением."""
    logger.debug("Команда /start от %s", update.effective_user.id)
    keyboard = [
        [InlineKeyboardButton("🎲 Рандомный факт", callback_data="random_fact")],
        [InlineKeyboardButton("🧠 ChatGPT", callback_data="gpt_interface")],
        [InlineKeyboardButton("🗣 Диалог с Войтенко", callback_data="talk_igor")],
        [InlineKeyboardButton("📚 Викторина", callback_data="quiz")],
        [InlineKeyboardButton("🏋️ Генератор тренировок", callback_data="training_plan")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome = (
        "<b>Добро пожаловать!</b>\nВыберите функцию ниже."
    )
    try:
        path = Path(__file__).parent.parent / "Images" / "menu.jpg"
        with open(path, "rb") as photo:
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=photo,
                caption=welcome,
                parse_mode="HTML",
                reply_markup=reply_markup
            )
    except FileNotFoundError:
        logger.warning("menu.jpg не найден")
        await update.message.reply_text(welcome, reply_markup=reply_markup, parse_mode="HTML")

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка нажатий из меню."""
    query = update.callback_query
    await query.answer()
    logger.debug("Кнопка %s от %s", query.data, update.effective_user.id)

    if query.data == "gpt_interface":
        context.user_data["awaiting_gpt"] = True
        await context.bot.send_message(chat_id=query.message.chat_id,
                                       text="🧠 Напиши свой вопрос:",
                                       parse_mode="HTML")
    # остальные варианты: random_fact, talk_igor, quiz, training_plan — вызывают свои модули
    # ...

async def return_to_main_menu(query):
    """Вернуться назад в меню."""
    await start(query, query._bot.get_context())  # просто вызвать start заново

def register_basic_handlers(d):
    d.add_handler(CommandHandler("start", start))
    d.add_handler(CallbackQueryHandler(menu_callback))














