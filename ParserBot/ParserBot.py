import asyncio
import hashlib
import sqlite3
import threading
import time
import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
import feedparser

# ---------- Константы для использования ----------
TOKEN = '8411974595:AAFairg4eftPoz6f4083mv_1RSygXg2vduY'
db_name = "tmp/ParserDB.db"
main_markup = (telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).row("/start").row("/news").
               row("/subscribe", "/unsubscribe"))
register_markup = (telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).row("/set_website lenta", "/set_website ria",
                                                                               "/set_website tass").
                   row("/set_website kommersant", "/set_website gazeta", "/set_website rbc"))
Websites = {"lenta": "https://lenta.ru/rss/news",
            "ria": "https://ria.ru/export/rss2/archive/index.xml",
            "tass": "https://tass.ru/rss/v2.xml",
            "kommersant": "https://www.kommersant.ru/rss/news.xml",
            "gazeta": "https://www.gazeta.ru/export/rss/first.xml",
            "rbc": "https://rssexport.rbc.ru/rbcnews/news/30/full.rss"}
bot = telebot.TeleBot(TOKEN)


# ---------- Создание БД ----------
def init_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS subscribers (
    chat_id TEXT    UNIQUE,
    number  INTEGER NOT NULL
    DEFAULT (5),
    website TEXT    NOT NULL
    DEFAULT lenta
    )""")
    conn.commit()
    conn.close()


# ---------- Работа с подписками ----------
def add_subscriber(chat_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO subscribers (chat_id) VALUES (?)", (chat_id,))
    conn.commit()
    conn.close()


def update_website_subscriber(chat_id, website):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE subscribers SET website = ? WHERE chat_id = ?", (website, chat_id))
    conn.commit()
    conn.close()


def update_number_subscriber(chat_id, number):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE subscribers SET number = ? WHERE chat_id = ?", (number, chat_id))
    conn.commit()
    conn.close()


def remove_subscriber(chat_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subscribers WHERE chat_id=?", (chat_id,))
    conn.commit()
    conn.close()


def get_subscribers():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT chat_id, number, website FROM subscribers")
    subs = [row for row in cursor.fetchall()]
    conn.close()
    return subs


# ---------- Парсинг новостей ----------
def get_news(new_url="https://lenta.ru/rss/news", number=5):
    feed = feedparser.parse(new_url)

    news = []
    for entry in feed.entries[:number + 1]:
        title = entry.get("title", "Без заголовка")
        summary = entry.get("summary", "Без описания")
        date = entry.get("published", "Дата не указана")
        link = entry.get("link", "Без ссылки")
        news.append(f"{title}!:{summary if len(summary) > 0 else 'Нет описания'}!:{date}!:{link}")
    return "\n".join(news)


# def get_news():
#     url = "https://lenta.ru"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     news = []
#     for item in soup.select("a.card-big__title")[:5]:  # другой селектор
#         title = item.get_text(strip=True)
#         link = url + item.get("href")
#         news.append(f"{title}\n{link}")
#     return "\n\n".join(news)

# ---------- Авто-рассылка ----------
def broadcast_news():
    try:
        subscribers = get_subscribers()
        for subscriber in subscribers:
            try:
                bot.send_message(subscriber[0], "📰 Свежие новости:")
                headlines = get_news(Websites[subscriber[2]], subscriber[1])
                if len(headlines) > 0:
                    ss = headlines.split("\n")
                    for i in ss:
                        s = i.split("!:")
                        mess = f"<b>{s[0]}</b>\n{s[1]}\n\n{s[2]}\n{s[3]}"
                        bot.send_message(subscriber[0], mess, reply_markup=main_markup, parse_mode='html')
                else:
                    bot.send_message(subscriber[0], "Новостей нет", reply_markup=main_markup, parse_mode='html')
            except Exception as e:
                print(f"Ошибка отправки в {subscriber[0]}: {e}")
    except Exception as e:
        print(f"Ошибка при получении новостей: {e}")
    # запускать каждые 30 минут
    threading.Timer(1800, broadcast_news).start()


# ---------- Команды ----------
@bot.message_handler(commands=["start"])
def start(message):
    mess = (f"Привет, <b><u>{message.from_user.username}</u></b>, я новостной бот.\n"
            f"/news — последние новости\n"
            f"/subscribe — подписаться на рассылку\n"
            f"/unsubscribe — отписаться от рассылки\n"
            f"Для лучшего понимания работы бота используйте функцию /help\n")
    bot.send_message(message.chat.id, mess, reply_markup=main_markup, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    with open("tmp/help.txt", mode="rb") as doc:
        bot.send_document(message.chat.id, doc, reply_markup=main_markup)


@bot.message_handler(commands=['news'])
def news(message):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    command = f"""SELECT chat_id FROM subscribers"""
    result = cur.execute(command).fetchall()
    result = [i[0] for i in result]
    con.close()
    if str(message.from_user.id) in result:
        mi1 = types.InlineKeyboardMarkup()
        i1 = types.InlineKeyboardButton(text='Lenta.ru', callback_data="s1")
        i2 = types.InlineKeyboardButton(text='RIA.ru', callback_data="s2")
        i3 = types.InlineKeyboardButton(text='TASS.ru', callback_data="s3")
        i4 = types.InlineKeyboardButton(text='Kommersant.ru', callback_data="s4")
        i5 = types.InlineKeyboardButton(text='Gazeta.ru', callback_data="s5")
        i6 = types.InlineKeyboardButton(text='RBC.ru', callback_data="s6")
        mi1.row(i1, i2, i3).row(i4, i5, i6)
        bot.send_message(message.chat.id,
                         f"Выберите сайт",
                         reply_markup=mi1, parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Вам нужно сначала подписаться на рассылку /subscribe",
                         reply_markup=main_markup, parse_mode='html')


@bot.message_handler(commands=["subscribe"])
def subscribe(message):
    add_subscriber(message.from_user.id)
    bot.send_message(message.chat.id, "✅ Вы подписаны на рассылку новостей!\nДавайте выберем сайт по умолчанию",
                     reply_markup=register_markup, parse_mode='html')


# функция-обработчик
@bot.message_handler(func=lambda message: message.text.startswith("/set_website"))
def set_website(message):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    command = f"""SELECT chat_id FROM subscribers"""
    result = cur.execute(command).fetchall()
    result = [i[0] for i in result]
    con.close()
    if str(message.from_user.id) in result:
        website_id = message.text.split()[1]
        if website_id in Websites.keys():
            update_website_subscriber(message.from_user.id, website_id)
            tb = bot.send_message(message.chat.id,
                                  "Напишите какое количество новостей вы хотите получать (от 1  до 10)",
                                  reply_markup=main_markup, parse_mode='html')
            bot.register_next_step_handler(tb, subscribe_2)
        else:
            bot.send_message(message.chat.id, "Такого сайта нет",
                             reply_markup=main_markup, parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Вам нужно сначала подписаться на рассылку /subscribe",
                         reply_markup=main_markup, parse_mode='html')


def subscribe_2(message):
    try:
        if int(message.text) > 10 or int(message.text) < 1:
            bot.send_message(message.chat.id, "Вы выбрали некорректное число, было выбрано по умолчанию 5",
                             reply_markup=main_markup, parse_mode='html')
        else:
            update_number_subscriber(message.from_user.id, int(message.text))
            bot.send_message(message.chat.id, f"Вы выбрали число {int(message.text)}",
                             reply_markup=main_markup, parse_mode='html')
    except Exception as e:
        bot.send_message(message.chat.id, "Вы выбрали некорректное число, было выбрано по умолчанию 5",
                         reply_markup=main_markup, parse_mode='html')


@bot.message_handler(commands=["unsubscribe"])
def unsubscribe(message):
    remove_subscriber(message.from_user.id)
    bot.send_message(message.chat.id, "❌ Вы отписались от рассылки.")


@bot.callback_query_handler(func=lambda call: True)
def task(call):
    website = ""
    if call.data == "s1":
        bot.answer_callback_query(call.id, "Вы выбрали Lenta.ru!", False)
        website = "lenta"
    elif call.data == "s2":
        bot.answer_callback_query(call.id, "Вы выбрали RIA.ru!", False)
        website = "ria"
    elif call.data == "s3":
        bot.answer_callback_query(call.id, "Вы выбрали TASS.ru!", False)
        website = "tass"
    elif call.data == "s4":
        bot.answer_callback_query(call.id, "Вы выбрали Kommersant.ru!", False)
        website = "kommersant"
    elif call.data == "s5":
        bot.answer_callback_query(call.id, "Вы выбрали Gazeta.ru!", False)
        website = "gazeta"
    elif call.data == "s6":
        bot.answer_callback_query(call.id, "Вы выбрали RBC.ru!", False)
        website = "rbc"

    if website != "":
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""SELECT number FROM subscribers WHERE chat_id = {call.message.chat.id}"""
        result = cur.execute(command).fetchall()
        result = int([i[0] for i in result][0])
        con.close()

        headlines = get_news(Websites[website], result if result != 0 else 5)
        if len(headlines) > 0:
            ss = headlines.split("\n")
            for i in ss:
                s = i.split("!:")
                mess = f"<b>{s[0]}</b>\n{s[1]}\n\n{s[2]}\n{s[3]}"
                bot.send_message(call.message.chat.id, mess, parse_mode='html')
        else:
            bot.send_message(call.message.chat.id, "Ошибка при получении новостей")


@bot.message_handler(content_types='sticker')
def dop_f1(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.emoji)


@bot.message_handler(content_types=['text', 'photo'])
def tekst(message):
    bot.send_message(message.chat.id, f"Тип сообщения: {message.content_type}")


def main():
    init_db()
    print("✅ Бот запущен...")
    broadcast_news()  # первый запуск авто-рассылки
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
    # Библиотека telebot (pyTelegramBotAPI) сама по себе не асинхронная, поэтому тебе не нужно asyncio.run(main()) и async def main().
    # Лучше просто написать обычную функцию main() и вызывать main().
