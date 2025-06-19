import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /start."""
    keyboard = [
        [InlineKeyboardButton("🎲 Рандомный факт", callback_data="random_fact")],
        [InlineKeyboardButton("🧠 ChatGPT", callback_data="gpt_interface")],
        [InlineKeyboardButton("🗣 Диалог с Войтенко", callback_data="talk_igor")],
        [InlineKeyboardButton("📚 Викторина", callback_data="quiz")],
        [InlineKeyboardButton("🏋️ Генератор тренировок", callback_data="training_plan")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "<b>Добро пожаловать в ChatGPT бота!</b>\n\n"
        "⚙️ Доступные функции:\n"
        "🎲 Рандомный факт — получи интересный факт\n"
        "🧠 ChatGPT — общение с ИИ\n"
        "🗣 Диалог с Войтенко — задавай вопросы мотивационному кумиру\n"
        "📚 Викторина — проверь свои знания\n"
        "🏋️ Генератор тренировок — индивидуальный план тренировок\n\n"
        "Выберите функцию из меню ниже!"
    )

    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="HTML")


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка нажатий на inline-кнопки."""
    query = update.callback_query
    await query.answer()

    if query.data == "random_fact":
        from handlers.random_fact import send_random_fact
        await send_random_fact(query, context)

    elif query.data == "gpt_interface":
        await query.edit_message_text(
            "🧠 Введите ваш вопрос для ChatGPT прямо в чат. Я отвечу!",
            parse_mode='HTML'
        )
        context.user_data['awaiting_gpt'] = True

    elif query.data == "talk_igor":
        from handlers.talk import start_talk_with_igor
        await start_talk_with_igor(query, context)

    elif query.data == "quiz":
        from handlers.quiz import start_quiz
        await start_quiz(query, context)

    elif query.data == "training_plan":
        from handlers.training import send_training_plan
        await send_training_plan(query, context)

    else:
        await query.edit_message_text("⚠️ Неизвестная команда.")
        return

    # Вернуть главное меню через 3 секунды
    await asyncio.sleep(3)
    await return_to_main_menu(query)


async def return_to_main_menu(query):
    """Возврат к главному меню."""
    keyboard = [
        [InlineKeyboardButton("🎲 Рандомный факт", callback_data="random_fact")],
        [InlineKeyboardButton("🧠 ChatGPT", callback_data="gpt_interface")],
        [InlineKeyboardButton("🗣 Диалог с Войтенко", callback_data="talk_igor")],
        [InlineKeyboardButton("📚 Викторина", callback_data="quiz")],
        [InlineKeyboardButton("🏋️ Генератор тренировок", callback_data="training_plan")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text="<b>Главное меню:</b>\nВыберите функцию ниже:",
        parse_mode="HTML",
        reply_markup=reply_markup
    )

