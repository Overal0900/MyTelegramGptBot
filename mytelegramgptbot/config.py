import os
from dotenv import load_dotenv

load_dotenv()

MYTG_BOT_TOKEN=os.getenv("MYTG_BOT_TOKEN")
CHAT_GPT_TOKEN=os.getenv("CHAT_GPT_TOKEN")

if not all([CHAT_GPT_TOKEN, MYTG_BOT_TOKEN]):
    raise ValueError("Введите токены в .env")

