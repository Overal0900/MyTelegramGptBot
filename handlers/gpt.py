import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes
from openai import OpenAI

# Загрузка переменных окружения
load_dotenv()
openai_token = os.getenv("CHAT_GPT_TOKEN")

# Инициализация клиента OpenAI
client = OpenAI(api_key=openai_token)


async def chat_with_gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    if not user_input:
        await update.message.reply_text("⚠️ Пожалуйста, введите текст для ChatGPT.")
        return

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты — умный Telegram-бот, помоги пользователю."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content.strip()
        await update.message.reply_text(answer)
    except Exception as e:
        await update.message.reply_text(f"❌ Ошибка при обращении к ChatGPT:\n\n{e}")


def register_gpt_handlers(app):
    # Пока всё реализуется в unknown_message, регистрировать нечего
    pass


