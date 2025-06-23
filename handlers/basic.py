import logging
import asyncio
from pathlib import Path
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /start."""
    logger.debug("Команда /start вызвана пользователем: %s", update.effective_user.id)

    keyboard = [
        [InlineKeyboardButton("🎲 Рандомный факт", callback_data="random_fact")],
        [InlineKeyboardButton("🧠 ChatGPT", callback_data="gpt_interface")],
        [InlineKeyboardButton("🗣 Диалог с Войтенко", callback_data="talk_igor")],
        [InlineKeyboardButton("📚 Викторина", callback_data="quiz")],
        [InlineKeyboardButton("🏋️ Генератор тренировок", callback_data="training_plan")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "<b>Добро пожаловать в GYM бота!</b>\n\n"
        "⚙️ Доступные функции:\n"
        "🎲 Рандомный факт — получи интересный факт\n"
        "🧠 ChatGPT — общение с ИИ\n"
        "🗣 Диалог с Войтенко — задавай вопросы мотивационному кумиру\n"
        "📚 Викторина — проверь свои знания\n"
        "🏋️ Генератор тренировок — индивидуальный план тренировок\n\n"
        "Выберите функцию из меню ниже!"
    )

    try:
        image_path = Path(__file__).parent.parent / "Images" / "menu.jpg"
        with open(image_path, "rb") as photo:
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=photo,
                caption=welcome_text,
                parse_mode="HTML",
                reply_markup=reply_markup
            )
    except FileNotFoundError:
        logger.warning("menu.jpg не найден. Отправка только текста.")
        await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="HTML")


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка нажатий на inline-кнопки."""
    query = update.callback_query
    await query.answer()
    user_id = update.effective_user.id
    logger.debug("Нажата кнопка: %s пользователем: %s", query.data, user_id)

    if query.data == "random_fact":
        from handlers.random_fact import send_random_fact
        await send_random_fact(query, context)
        await asyncio.sleep(2)
        await return_to_main_menu(query)

    elif query.data == "gpt_interface":
        logger.debug("Переход в режим GPT ввода")
        context.user_data["awaiting_gpt"] = True  # <- Эта строка добавлена
        await query.answer()
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="🧠 Введите ваш вопрос для ChatGPT прямо в чат. Я отвечу!",
            parse_mode='HTML'
        )

    elif query.data == "talk_igor":
        from handlers.talk import start_talk_with_igor
        await start_talk_with_igor(query, context)
        await asyncio.sleep(2)
        await return_to_main_menu(query)

    elif query.data == "quiz":
        from handlers.quiz import start_quiz
        await start_quiz(query, context)

    elif query.data.startswith("quiz_answer:"):
        from handlers.quiz import handle_quiz_answer
        await handle_quiz_answer(update, context)

    elif query.data == "training_plan":
        from handlers.training import send_training_plan
        await send_training_plan(query, context)
        await asyncio.sleep(2)
        await return_to_main_menu(query)

    else:
        logger.warning("Неизвестная callback_data: %s", query.data)
        await query.edit_message_text("⚠️ Неизвестная команда.")


async def return_to_main_menu(query):
    """Возврат к главному меню."""
    logger.debug("Возврат к главному меню для пользователя: %s", query.from_user.id)

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


def register_basic_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(menu_callback))














