from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
import asyncio

quiz_questions = [
    {
        "question": "🏋️ Кто из этих блогеров известен своим лозунгом 'БЕЗ ОТГОВОРОК'?",
        "options": ["Игорь Войтенко", "Шах", "Алексей Столяров", "Кирилл Сарычев"],
        "correct": "Игорь Войтенко"
    },
    {
        "question": "🔥 Кто из них известен как бодибилдер, популярный в TikTok, с креативными тренировками?",
        "options": ["Шах", "Сарычев", "Столяров", "Войтенко"],
        "correct": "Шах"
    },
    {
        "question": "💪 Кто является профессиональным пауэрлифтером и рекордсменом по жиму лёжа?",
        "options": ["Алексей Столяров", "Игорь Войтенко", "Шах", "Кирилл Сарычев"],
        "correct": "Кирилл Сарычев"
    }
]

async def start_quiz(query, context):
    context.user_data["quiz_index"] = 0
    context.user_data["quiz_score"] = 0
    await send_next_question(query, context)

async def send_next_question(query_or_update, context):
    index = context.user_data["quiz_index"]
    if index >= len(quiz_questions):
        score = context.user_data["quiz_score"]
        await query_or_update.edit_message_text(
            f"✅ Викторина завершена! Ваш результат: {score}/{len(quiz_questions)}.",
            parse_mode="HTML"
        )
        await asyncio.sleep(2)
        from handlers.basic import return_to_main_menu
        await return_to_main_menu(query_or_update)
        return

    question_data = quiz_questions[index]
    buttons = [
        [InlineKeyboardButton(option, callback_data=f"quiz_answer:{option}")]
        for option in question_data["options"]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await query_or_update.edit_message_text(
        question_data["question"],
        reply_markup=reply_markup
    )

async def handle_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_answer = query.data.split(":")[1]
    index = context.user_data.get("quiz_index", 0)
    correct_answer = quiz_questions[index]["correct"]

    if user_answer == correct_answer:
        context.user_data["quiz_score"] += 1
        response_text = "✅ Правильно!"
    else:
        response_text = f"❌ Неправильно! Верный ответ: {correct_answer}"

    await query.edit_message_text(response_text)
    context.user_data["quiz_index"] += 1

    await asyncio.sleep(2)
    await send_next_question(query, context)
