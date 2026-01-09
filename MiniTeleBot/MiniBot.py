import asyncio
import random
import requests
from datetime import time

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# =======================
# 🔑 НАСТРОЙКИ
# =======================

TELEGRAM_TOKEN = '8465295022:AAGuWUwBEg0Cgte3Qa66ehuJUZpz560NEd0'
GIPHY_API_KEY = "0RqPL06VxBzUsmccUTp3Whzz9SR2ncSA"

# =======================
# 💌 ТЕКСТЫ
# =======================

START_MESSAGE = (
    "Привет ☀️\n\n"
    "Я маленький бот, который будет иногда напоминать тебе, "
    "какая ты замечательная 💖\n\n"
    "Я буду присылать тёплые слова, гифки и маленькие советы ✨\n"
    "Ты можешь писать мне в любой момент 🌷"
)

SWEET_MESSAGES = [
    "💖 Пусть сегодня у тебя будет хотя бы один повод улыбнуться",
    "☀️ Ты заслуживаешь всего самого доброго",
    "🌷 Я надеюсь, ты сегодня бережёшь себя",
    "✨ Ты правда делаешь этот мир лучше",
    "💫 Даже если день сложный — ты справляешься",
]

ADVICE_MESSAGES = [
    "💡 Совет дня:\nСегодня сделай что-нибудь приятное для себя 🌸",
    "💡 Совет дня:\nНе торопись. Ты не опаздываешь 💗",
    "💡 Совет дня:\nИногда отдых — это тоже продуктивно ☁️",
]

REPLY_MESSAGES = [
    "💗 Мне приятно, что ты мне написала",
    "🌷 Я тебя услышал",
    "✨ Ты можешь писать мне в любой момент",
    "☁️ Надеюсь, у тебя сейчас всё хорошо",
]

# =======================
# 🎞️ GIPHY
# =======================

def get_random_gif():
    tags = ["cute", "love", "hug", "cat", "soft"]
    tag = random.choice(tags)

    url = "https://api.giphy.com/v1/gifs/random"
    params = {
        "api_key": GIPHY_API_KEY,
        "tag": tag,
        "rating": "g",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        return data["data"]["images"]["original"]["url"]
    except Exception:
        return None

# =======================
# ⏰ ПЕРИОДИЧЕСКИЕ ЗАДАЧИ
# =======================

async def send_sweet_message(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=random.choice(SWEET_MESSAGES),
    )

async def send_advice(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=random.choice(ADVICE_MESSAGES),
    )

async def send_gif(context: ContextTypes.DEFAULT_TYPE):
    gif_url = get_random_gif()

    if gif_url:
        await context.bot.send_animation(
            chat_id=context.job.chat_id,
            animation=gif_url,
        )
    else:
        await context.bot.send_message(
            chat_id=context.job.chat_id,
            text="🐾 Сегодня гифка немного задержалась, но я всё равно рядом 💖",
        )

# =======================
# 📩 /start
# =======================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    await update.message.reply_text(START_MESSAGE)

    # ❗ чтобы не создавать дубликаты задач
    if context.chat_data.get("jobs_started"):
        return

    context.chat_data["jobs_started"] = True

    context.job_queue.run_repeating(
        send_sweet_message,
        interval=60 * 60 * 4,
        first=30,
        chat_id=chat_id,
    )

    context.job_queue.run_repeating(
        send_gif,
        interval=60 * 60 * 6,
        first=120,
        chat_id=chat_id,
    )

    context.job_queue.run_daily(
        send_advice,
        time=time(hour=10, minute=0),
        chat_id=chat_id,
    )

# =======================
# 💬 СООБЩЕНИЯ
# =======================

async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if any(word in text for word in ["груст", "плохо", "устала"]):
        reply = "💔 Мне жаль это слышать. Ты не обязана быть сильной всё время"
    elif "спасибо" in text:
        reply = "💖 Всегда пожалуйста"
    elif "люблю" in text:
        reply = "🥺 Это очень тепло"
    elif "привет" in text:
        reply = "☀️ Привет-привет"
    else:
        reply = random.choice(REPLY_MESSAGES)

    await update.message.reply_text(reply)

# =======================
# 🚀 ЗАПУСК
# =======================
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_message))

    print("💖 Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
