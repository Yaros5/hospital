from typing import ItemsView
from telebot import types
import telebot
import sqlite3

TOKEN = "2142529380:AAH9OvlYi9zcii99FWijDrQiVhwGOjuFRn0"
bot = telebot.TeleBot(TOKEN)


# ! start
@bot.message_handler(commands=["start", "help"])
def start_message(message):
    global cursor, connect
    bot.remove_webhook()
    # remove keyboard
    connect = sqlite3.connect('server.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Oleh (login TEXT,password TEXT)''')
    connect.commit()
    remove_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "*Hello, {0.first_name} 👋*".format(message.from_user, bot.get_me()),
                     reply_markup=remove_keyboard, parse_mode="Markdown")
    bot.send_message(message.chat.id, "*If you are a doctor, then you can view the schedule of your patients here*",
                     parse_mode="Markdown")
    change_name(message)


# ! change name
def change_name(message):
    # remove keyboard
    remove_keyboard = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, "Send me your *full name*", parse_mode="Markdown",
                           reply_markup=remove_keyboard)
    bot.register_next_step_handler(msg, verification)


# ! verification
def verification(message):
    bot.send_message(message.chat.id, f"*Your name is {message.text}*", parse_mode="Markdown")
    login_from_bot = message.text
    print(f"User login from bot: {login_from_bot}")
    cursor.execute(f"SELECT id FROM Oleh WHERE login = {login_from_bot}")
    data = cursor.fetchall()
    if  cursor.fetchone() is None:
        bot.send_message('такого корситувача не існує')

    global db, sql
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute('''CREATE TABLE IF NOT EXISTS users (
    login Text,
    password Text,
    cash int
    )''')
    db.commit()

    sql.execute(f'SELECT login FROM users WHERE login = "{login_from_bot}" ')
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)" , (login_from_bot, 1111, 0))
        db.commit()
        print("Вас успішно зарегестровано")
        bot.send_message(message.chat.id, "*[Вас успішно зарегестровано]*", parse_mode="Markdown")

    else:
        print("Такий акаунт вже існує")
        bot.send_message(message.chat.id, "*[Такий акаунт вже існує]*", parse_mode="Markdown")


# ! buttons
@bot.message_handler(content_types=["text"])
def buttons(message):
    # ! ADMIN
    # / remove webhook
    if message.text == "remove_webhook":
        bot.delete_message(message.chat.id, message.message_id)
        bot.remove_webhook()
    # / stop polling
    elif message.text == "stop_polling":
        bot.delete_message(message.chat.id, message.message_id)
        bot.stop_bot()
    # / secret
    elif message.text == "CHOSEN ONES":
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "*CHOSEN ONES ARE THE BEST!*", parse_mode="Markdown")
    # ! change name
    elif message.text == "✒️ Change name":
        change_name(message)
    # ! schedule
    elif message.text == "📰 Schedule":
        bot.send_message(message.chat.id, "*Schedule of your patients:*", parse_mode="Markdown")
        # example
        bot.send_message(message.chat.id, "Patient 1")
        bot.send_message(message.chat.id, "Patient 2")
        bot.send_message(message.chat.id, "Patient 3")


# ! polling
bot.infinity_polling()