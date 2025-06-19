import random

facts = [
    "🐝 Пчёлы могут распознавать лица.",
    "🌌 Во Вселенной больше звёзд, чем песчинок на Земле.",
    "🐙 У осьминога три сердца.",
    "🔥 Самая горячая температура, зарегистрированная на Земле, — 56.7°C.",
]

async def send_random_fact(query, context):
    fact = random.choice(facts)
    await query.edit_message_text(f"🎲 Случайный факт:\n\n{fact}")
