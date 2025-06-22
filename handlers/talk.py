from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
import openai
import os

# Инициализация OpenAI токена (предполагается, что переменная окружения OPENAI_API_KEY уже настроена)
openai.api_key = os.getenv("CHAT_GPT_TOKEN")


async def start_talk_with_igor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗣 Ты начал диалог с Игорем Войтенко!\n\n"
        "Напиши свой вопрос сюда, и я отвечу от его имени."
    )
    context.user_data["awaiting_igor"] = True  # ✅ Запоминаем, что ждём вопроса для Войтенко


async def handle_igor_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка сообщений для Игоря Войтенко через ChatGPT."""
    if context.user_data.get("awaiting_igor"):
        user_input = update.message.text

        # Формируем системное сообщение для ChatGPT с персоной Игоря Войтенко
        system_prompt = (
            "Ты — Игорь Войтенко, мотивационный тренер и бизнесмен, говоришь энергично, "
            "дисциплинированно, поддерживающе и прямо. "
            "Отвечай кратко, но вдохновляюще."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # или "gpt-4" если есть доступ
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=200,
                temperature=0.7,
            )

            answer = response.choices[0].message.content.strip()

        except Exception as e:
            answer = "⚠️ Ошибка при запросе к ChatGPT. Попробуй позже."

        await update.message.reply_text(answer, parse_mode="HTML")
        # Оставляем сессию открытой, чтобы можно было продолжить диалог
        # Если хочешь закрывать после одного сообщения — раскомментируй следующую строку
        # context.user_data["awaiting_igor"] = False


def register_talk_handlers(app: Application):
    """Регистрируем обработчики, связанные с разговором с Игорем Войтенко."""
    app.add_handler(CommandHandler("startigor", start_talk_with_igor))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_igor_message))

