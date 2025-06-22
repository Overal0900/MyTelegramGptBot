import random

training_plans = [
    "🏋️ 3x10 приседаний\n💪 3x12 отжиманий\n🧘 5 минут планки",
    "💥 Бёрпи 3 подхода по 15\n🚴 Велотренажёр 20 минут\n🧘 Йога 10 минут",
    "🏃 Интервальный бег 15 минут\n🦵 Выпады с гантелями 3x10\n🧘 Растяжка",
]

async def send_training_plan(query, context):
    plan = random.choice(training_plans)
    await query.edit_message_text(f"🏋️ Твоя тренировка на сегодня:\n\n{plan}")


def register_workout_handlers(app):
    pass  # всё вызывается из basic
