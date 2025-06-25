# MyTelegramGptBot

# Telegram GPT Бот 🤖🧠

Этот бот — простой Telegram-интерфейс для общения с ChatGPT. Он поддерживает команды, генерацию тренировок, квизы, режим общения с известными личностями (например, Игорем Войтенко), и может быть легко расширен.

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/username/mytelegramgptbot.git
cd mytelegramgptbot
2. Установка зависимостей
Рекомендуется использовать виртуальное окружение:

bash
Копировать
Редактировать
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Установи зависимости:

bash
Копировать
Редактировать
pip install -r requirements.txt
3. Настройка токенов
Создай следующие файлы в корне проекта:

telegram-token.txt — сюда помести токен Telegram-бота

openai-token.txt — сюда помести OpenAI API ключ

4. Запуск бота
bash
Копировать
Редактировать
python main.py
🧠 Возможности
Бот умеет:

/start — показать главное меню

/gpt — задать вопрос ChatGPT

/random — получить случайный факт

/workout — сгенерировать тренировку

/quiz — пройти квиз по спорту

/talk — поговорить с "Игорем Войтенко" (ролевая игра)

Расширяемая структура: можно добавлять новые команды и режимы

📂 Структура проекта
bash
Копировать
Редактировать
mytelegramgptbot/
│
├── handlers/               # Все обработчики команд
│   ├── gpt_handler.py
│   ├── quiz_handler.py
│   └── ...
│
├── services/               # Бизнес-логика и взаимодействие с API
│   ├── openai_service.py
│   └── ...
│
├── utils/                  # Утилиты и вспомогательные функции
│   └── ...
│
├── main.py                 # Точка входа
├── __init__.py             # Инициализация пакета
├── telegram-token.txt      # Токен Telegram-бота (не коммитить!)
├── openai-token.txt        # Токен OpenAI (не коммитить!)
└── requirements.txt        # Зависимости
🛡️ Безопасность
Убедись, что .gitignore содержит:

gitignore
Копировать
Редактировать
telegram-token.txt
openai-token.txt
.idea/
🛠️ TODO / Идеи
 Добавить логирование всех действий

 Реализовать историю чатов

 Поддержка нескольких языков

 Панель администратора

🤝 Контакты
Автор: Филипп Челухин
Telegram-бот: @THE_BEST_GYM_BOT
