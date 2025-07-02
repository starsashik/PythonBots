# Очень важные импорты
import asyncio
import hashlib
import sqlite3

import telebot
from telebot import types
import requests

# константы для использования
TOKEN = '7790194799:AAGm8OPcfu-j5QgKcPYa3GRmU0JsmuooSz8'
db_name = "rofltmp/RoflTeleBotDB.db"

GIPHY_URL = "http://api.giphy.com/v1/gifs/random"
GIPHY_API_KEY = "0RqPL06VxBzUsmccUTp3Whzz9SR2ncSA"

# Reply клавиатуры
start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start_markup.row("/logIn")
start_markup.row('/registration')
start_markup.row("/help")

main_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.add("/Tasks")
main_markup.row('/profile', "/logOut")

tasks_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
tasks_markup.add("/task1").add('/gif_r', "/gif_s").add("/back")



# главная фунция в которой работает бот
async def main():
    bot = telebot.TeleBot(TOKEN)
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    command = f"""SELECT id FROM User"""
    result = cur.execute(command).fetchall()
    con.close()
    dd = {i[0]: False for i in result}
    print(dd)

    # функция для началы работы бота
    @bot.message_handler(commands=["start"])
    def start(message):
        mess = f"Привет, <b><u>{message.from_user.username}</u></b>, Я бот помощник для Star.\n" \
               f"Для удобной работы со мной, лучше всего зарегистрироваться\n" \
               f"Если у вас уже есть аккаунт, то можете войти в него. /logIn\n" \
               f"Для лучшего понимания работы бота используйте функцию /help\n",
        bot.send_message(message.chat.id, mess, reply_markup=start_markup, parse_mode='html')

    # функция для вызова файла с инструкцией по использоавнию
    @bot.message_handler(commands=['help'])
    def help(message):
        doc = open("tmp/help.txt", mode="rb")
        bot.send_document(message.chat.id, doc)
        doc.close()

    # функция для скрытия клавиатуры
    @bot.message_handler(commands=['close'])
    def close(message):
        bot.send_message(message.chat.id, "Клавиатура скрыта", reply_markup=telebot.types.ReplyKeyboardRemove())

    # функция для перехода в меню заданий
    @bot.message_handler(commands=['back'])
    def bacc(message):
        bot.send_message(message.chat.id, "Вы вернулись в основное меню", reply_markup=main_markup, parse_mode='html')

    # функции для регистрации
    @bot.message_handler(commands=["registration"])
    def reg1(message):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""SELECT id FROM User"""
        result = cur.execute(command).fetchall()
        result = [i[0] for i in result]
        con.close()
        if int(message.from_user.id) in result:
            bot.send_message(message.chat.id, "Пользователь с вашем id уже зарегистрирован")
        else:
            tb = bot.send_message(message.chat.id, "Придумайте и отправьте пароль.\n"
                                                   "Хорошо запомните его, так как его нельзя будет восстановить.")
            bot.register_next_step_handler(tb, reg2)

    def reg2(message):
        passwords = "b" + message.text
        password = hashlib.md5(passwords.encode("utf8"))
        bot.delete_message(message.chat.id, message.message_id)
        
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""INSERT INTO User  VALUES(?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), message.from_user.username, password.hexdigest()))
        command = f"""INSERT INTO Task1  VALUES(?, ?, ?, ?, ?);"""
        cur.execute(command, (int(message.from_user.id), 0, 0, 0, 0))

        con.commit()
        con.close()
        
        bot.send_message(message.chat.id, f"Добро пожаловать, <b><u>{message.from_user.username}</u></b>!",
                         parse_mode='html',
                         reply_markup=main_markup)
        dd[int(message.from_user.id)] = True

    # функции для входа в систему
    @bot.message_handler(commands=["logIn"])
    def login(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, вы уже вошли в аккаунт, "
                                 f"можете приступать к выполнению заданий\n(снизу)",
                                 reply_markup=main_markup, parse_mode='html')
            else:
                tb = bot.send_message(message.chat.id, "Пароль:")
                bot.register_next_step_handler(tb, log2)

        except KeyError:
            bot.send_message(message.chat.id, f"Аккаунта с вашем логином не существуют.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    def log2(message):
        passwords = "b" + message.text
        password = hashlib.md5(passwords.encode("utf8"))
        bot.delete_message(message.chat.id, message.message_id)
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""SELECT password FROM User WHERE id = {int(message.from_user.id)}"""
        result = cur.execute(command).fetchall()
        con.close()
        if password.hexdigest() == result[0][0]:
            dd[int(message.from_user.id)] = True
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы успешно вошли в аккаунт, "
                             f"можете приступать к выполнению заданий\n(смотрите клавиатуру)",
                             reply_markup=main_markup, parse_mode='html')
        else:
            bot.send_message(message.chat.id, f"Пароль неверный.\n"
                                              f"Попробуйте еще раз /login \n"
                                              f"Если вы забыли пароль, то к сожалению вам придется удалить аккаунт.\n"
                                              f"Для этого напишите '/del_acc'",
                             reply_markup=start_markup)

    # функция для выхода из системы
    @bot.message_handler(commands=["logOut"])
    def logout(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                dd[int(message.from_user.id)] = False
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, вы успешно вышли из аккаунта",
                                 reply_markup=start_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, вы и так были не в сети",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Аккаунта с вашем логином не существуют.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    # функции для удаления аккаунта
    @bot.message_handler(commands=['del_acc'])
    def del_acc(message):
        img = open("tmp/dpf.jpg", mode="rb")
        bot.send_photo(message.chat.id, img)
        img.close()
        tb = bot.send_message(message.chat.id, "Для подтверждения удаления аккаунта введите то, что увидите на фото")
        bot.register_next_step_handler(tb, del_acc2)

    def del_acc2(message):
        if message.text == ">Delete.":
            if int(message.from_user.id) in dd:
                con = sqlite3.connect(db_name)
                cur = con.cursor()
                command = f"""DELETE FROM User WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                command = f"""DELETE FROM Task1 WHERE id = {int(message.from_user.id)}"""
                cur.execute(command)
                con.commit()
                con.close()

                dd.pop(int(message.from_user.id))
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, ваш аккаунт был удален:)",
                                 reply_markup=start_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"У вас нет аккаунта для удаления:/",
                                 reply_markup=start_markup, parse_mode='html')
        else:
            bot.send_message(message.chat.id,
                             f"Вы ввели неправильное контрольное слово",
                             reply_markup=start_markup, parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id)


    # функция для показа профиля пользователя
    @bot.message_handler(commands=['profile'])
    def prof(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                con = sqlite3.connect(db_name)
                cur = con.cursor()
                d = []
                for i in range(1, 2):
                    command1 = f"""Select Total FROM Task{i} WHERE id = {int(message.from_user.id)}"""
                    res = cur.execute(command1).fetchone()
                    d.append(res[0])
                con.close()
                bot.send_message(message.chat.id,
                                 f"<b>{message.from_user.username}: {message.from_user.first_name} "
                                 f"{message.from_user.last_name if message.from_user.last_name is not None else ''}"
                                 f"</b>\n Анализ информационных моделей - {d[0]}%\n",
                                 reply_markup=main_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b> чтобы посмотреть свой профиль "
                                 f"залогинтесь\n "
                                 f"/logIn",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"У вас еще нет профиля, сначала зарегистрируйтесь.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    # функции для перехода между блоками заданий
    @bot.message_handler(commands=["Tasks"])
    def tasks(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, пожалуйста выбирайте:",
                                 reply_markup=tasks_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий. /logIn",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    # функции для вывода заданий
    @bot.message_handler(commands=['task1'])
    def task1(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                mi1 = types.InlineKeyboardMarkup()
                i1 = types.InlineKeyboardButton(text='Неоднозначное соотнесение таблицы и графа', callback_data="t1_1")
                i2 = types.InlineKeyboardButton(text='Однозначное соотнесение таблицы и графа', callback_data="t1_2")
                i3 = types.InlineKeyboardButton(text='Поиск оптимального маршрута по таблице', callback_data="t1_3")
                mi1.add(i1).add(i2).add(i3)
                bot.send_message(message.chat.id,
                                 f"Задание 1:\n<u>Анализ информационных моделей</u>\n",
                                 reply_markup=mi1, parse_mode='html')
            else:
                bot.send_message(message.chat.id,
                                 f"<b><u>{message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий. /logIn",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(message.chat.id, f"Вы не можете приступить к заданиям без регистрации.\n"
                                              f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    # функции для проверки ответов
    def t1_1A(message):
        with open("tmp/Task1/1/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task1" SET "1" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t1_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", reply_markup=tasks_markup, parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t1_1R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t1_2A(message):
        with open("tmp/Task1/2/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task1" SET "2" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t1_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", reply_markup=tasks_markup, parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t1_2R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t1_3A(message):
        with open("tmp/Task1/3/answer", encoding='utf8') as f:
            d = f.readline()
        if message.text == d:
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            command = f"""UPDATE "Task1" SET "3" = '1' WHERE id = {int(message.from_user.id)}"""
            cur.execute(command)
            con.commit()
            cur.close()
            t1_up(int(message.from_user.id))
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы правильно решили задачу\n"
                             f"Ваш результат учтен", reply_markup=tasks_markup, parse_mode='html')
        else:
            mi1 = types.InlineKeyboardMarkup()
            i1 = types.InlineKeyboardButton(text='Решение', callback_data="t1_3R")
            mi1.add(i1)
            bot.send_message(message.chat.id,
                             f"<b><u>{message.from_user.username}</u></b>, вы ответили <b>неверно</b>.\n"
                             f"Можете посмотреть решение",
                             reply_markup=mi1, parse_mode='html')

    def t1_up(idd):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        command = f"""Select * from Task1 WHERE id = {idd}"""
        result = cur.execute(command).fetchall()
        curent = round(sum(result[0][1:4]) / 3 * 100)
        command = f"""UPDATE "Task1" SET "Total" = {curent} WHERE id = {idd}"""
        cur.execute(command)
        con.commit()
        cur.close()

        # функции для регистрации
    @bot.message_handler(commands=["gif_s"])
    def gif_s(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                tb = bot.send_message(message.chat.id, "Что вы хотите найти?")
                bot.register_next_step_handler(tb, gif_s2)
            else:
                bot.send_message(message.chat.id, f"/logIn",
                                 reply_markup=start_markup)
        except KeyError:
            bot.send_message(message.chat.id, f"/start",
                         reply_markup=start_markup)

    def gif_s2(message):
        try:
            text = " ".join(message.text)
            params = {'api_key': GIPHY_API_KEY,
                      'tag': text,
                      'rating': 'r'}
            response = requests.request("GET", GIPHY_URL, params=params).json()
            gif_url = response["data"]["url"]

            bot.send_message(message.chat.id, gif_url, reply_markup=tasks_markup, parse_mode='html')
            bot.send_message(message.chat.id, message.text, reply_markup=tasks_markup, parse_mode='html')
        except Exception:
            bot.send_message(message.chat.id, "Ошибка", reply_markup=tasks_markup, parse_mode='html')

    @bot.message_handler(commands=["gif_r"])
    def gif_r(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                try:
                    params = {'api_key': GIPHY_API_KEY,
                              'rating': 'r'}
                    response = requests.request("GET", GIPHY_URL, params=params).json()
                    gif_url = response["data"]["url"]

                    bot.send_message(message.chat.id, gif_url, reply_markup=tasks_markup, parse_mode='html')
                except Exception:
                    bot.send_message(message.chat.id, "Ошибка", reply_markup=tasks_markup, parse_mode='html')
            else:
                bot.send_message(message.chat.id, f"/logIn",
                                 reply_markup=start_markup)
        except KeyError:
            bot.send_message(message.chat.id, f"/start",
                         reply_markup=start_markup)

    # функция для отработки callback"ов (меню заданий)
    @bot.callback_query_handler(func=lambda call: True)
    def task(call):
        idd = call.message.chat.id
        try:
            current = dd[int(call.from_user.id)]
            if current:
                if call.data == "t1_1":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_1A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t1_1R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task1/1/task.png", "rb")
                    bot.send_message(idd, f"Задание 1.1:\n<b>Неоднозначное соотнесение таблицы и графа</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t1_1A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t1_1A)
                if call.data == "t1_1R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_1A")
                    mi1.add(i1)
                    with open("tmp/Task1/1/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task1/1/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 1.1\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t1_2":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_2A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t1_2R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task1/2/task.png", "rb")
                    bot.send_message(idd, f"Задание 1.2:\n<b>Однозначное соотнесение таблицы и графа</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t1_2A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t1_2A)
                if call.data == "t1_2R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_2A")
                    mi1.add(i1)
                    with open("tmp/Task1/2/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task1/2/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 1.2\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

                if call.data == "t1_3":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_3A")
                    i2 = types.InlineKeyboardButton(text='Решение', callback_data="t1_3R")
                    mi1.add(i1).add(i2)
                    phot = open("tmp/Task1/3/task.png", "rb")
                    bot.send_message(idd, f"Задание 1.3:\n<b>Поиск оптимального маршрута по таблице</b>",
                                     parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()
                if call.data == "t1_3A":
                    tb = bot.send_message(idd,
                                          "Ваш ответ:\n(это должно быть целое число, "
                                          "запишите его без лишних запятых и знаков. Например: 25)")
                    bot.register_next_step_handler(tb, t1_3A)
                if call.data == "t1_3R":
                    mi1 = types.InlineKeyboardMarkup()
                    i1 = types.InlineKeyboardButton(text='Ответить', callback_data="t1_3A")
                    mi1.add(i1)
                    with open("tmp/Task1/3/answer", encoding='utf8') as f:
                        d = f.read().split("\n")
                    phot = open('tmp/Task1/3/solution.png', "rb")
                    bot.send_message(idd, f"<b>Решение</b> задания 1.3\n<b>Ответ:</b> {' '.join(d)}", parse_mode='html')
                    bot.send_photo(idd, phot, reply_markup=mi1)
                    phot.close()

            else:
                bot.send_message(idd,
                                 f"<b><u>{call.message.from_user.username}</u></b>, войдите в свой аккаунт "
                                 f"для решения заданий. /logIn",
                                 reply_markup=start_markup, parse_mode='html')

        except KeyError:
            bot.send_message(idd, f"Вы не можете приступить к заданиям без регистрации.\n"
                                  f"Для регистрации воспользуйтесь функцией /registration",
                             reply_markup=start_markup)

    # функция для шутки над пользователем
    @bot.message_handler(content_types='sticker')
    def dop_f1(message):
        bot.send_sticker(message.chat.id, message.sticker.file_id)
        bot.send_message(message.chat.id, message.sticker.emoji)

    # функция для обработки неизвестных сообщений
    @bot.message_handler(content_types=['text', 'photo'])
    def tekst(message):
        try:
            current = dd[int(message.from_user.id)]
            if current:
                bot.send_message(message.chat.id, f"Если вам что-то непонятно /help",
                                 reply_markup=main_markup)
            else:
                bot.send_message(message.chat.id, f"/logIn",
                                 reply_markup=start_markup)
        except KeyError:
            bot.send_message(message.chat.id, f"/start",
                             reply_markup=start_markup)

    bot.polling(none_stop=True)


if __name__ == '__main__':
    asyncio.run(main())
