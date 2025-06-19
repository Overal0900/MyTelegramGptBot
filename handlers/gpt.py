import openai
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes

load_dotenv()
openai_api_key = os.getenv("CHAT_GPT_TOKEN")


async def chat_with_gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ты — умный Telegram-бот, помоги пользователю."},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content
    await update.message.reply_text(answer)