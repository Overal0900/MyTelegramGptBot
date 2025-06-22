import logging

from .random_fact import register_random_fact_handlers
from .training import register_workout_handlers
from .talk import register_talk_handlers
from .gpt import register_gpt_handlers
from .basic import register_basic_handlers  # Если понадобится расширение

logger = logging.getLogger(__name__)


def register_all_handlers(app):
    logger.info("🔁 Регистрация всех обработчиков...")

    register_random_fact_handlers(app)
    logger.info("✅ Обработчики рандомных фактов зарегистрированы")

    register_workout_handlers(app)
    logger.info("✅ Обработчики тренировок зарегистрированы")

    register_talk_handlers(app)
    logger.info("✅ Обработчики диалога с Войтенко зарегистрированы")

    register_gpt_handlers(app)
    logger.info("✅ Обработчики ChatGPT зарегистрированы")

    # register_basic_handlers(app) — уже зарегистрированы вручную в main.py
    logger.info("🎯 Все обработчики успешно зарегистрированы")
