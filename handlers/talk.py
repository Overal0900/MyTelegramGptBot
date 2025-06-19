async def start_talk_with_igor(query, context):
    await query.edit_message_text(
        "🗣 Ты начал диалог с Игорем Войтенко!\n\n"
        "Напиши свой вопрос сюда, и я отвечу от его имени.",
        parse_mode="HTML"
    )
    context.user_data["talking_to_igor"] = True