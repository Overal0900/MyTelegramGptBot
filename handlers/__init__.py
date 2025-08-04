"""Регистрируем обработчики для разных модулей."""
import logging
from .random_fact import register_random_fact_handlers
from .training import register_workout_handlers
from .talk import register_talk_handlers
from .gpt import register_gpt_handlers

logger = logging.getLogger(__name__)

def register_all_handlers(app):
    logger.info("🔁 Регистрируем обработчики...")
    register_random_fact_handlers(app)
    register_workout_handlers(app)
    register_talk_handlers(app)
    register_gpt_handlers(app)
    logger.info("🎯 Все обработчики зарегистрированы.")
