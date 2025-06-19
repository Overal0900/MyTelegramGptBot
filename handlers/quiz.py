async def start_quiz(query, context):
    await query.edit_message_text(
        "📚 Викторина скоро начнётся! Пока в разработке, но скоро будет доступна.",
        parse_mode="HTML"
    )