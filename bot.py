from typing import ItemsView
from telebot import types
import telebot
# import sqlite3
import os
import shutil
import time

TOKEN = "2142529380:AAH9OvlYi9zcii99FWijDrQiVhwGOjuFRn0"
bot = telebot.TeleBot(TOKEN)

while True:
    # ! start
    @bot.message_handler(commands=["start", "help"])
    def start_message(message):
        # remove keyboard
        remove_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "*Hello, {0.first_name} 👋*".format(message.from_user, bot.get_me()), reply_markup=remove_keyboard, parse_mode="Markdown")
        bot.send_message(message.chat.id, "*If you are a doctor, then you can view the schedule of your patients here*", parse_mode="Markdown")
        # / nickname
        global id_from_bot
        nickname_from_bot = message.from_user.first_name
        print(f"User nickname: {nickname_from_bot}")
        # / username
        global id_from_bot
        username_from_bot = message.from_user.username
        print(f"User username: {username_from_bot}")
        # / id
        global id_from_bot
        id_from_bot = message.from_user.id
        print(f"User id: {id_from_bot}")
        login_ask(message)


    # ! login_ask
    def login_ask(message):
        bot.send_message(message.chat.id, "Send me your *login*", parse_mode="Markdown")
        # goto login_ask_complete
        bot.register_next_step_handler(message, login_ask_complete)
    def login_ask_complete(message):
        # / login
        global login_from_bot
        login_from_bot = message.text
        print(f"User login: {login_from_bot}")
        # goto password_ask
        password_ask(message)


    # ! password_ask
    def password_ask(message):
        bot.send_message(message.chat.id, "Send me your *password*", parse_mode="Markdown")
        # goto password_ask_complete
        bot.register_next_step_handler(message, password_ask_complete)
    def password_ask_complete(message):
        # / password
        global password_from_bot
        password_from_bot = message.text
        print(f"User password: {password_from_bot}\n")
        # goto signup_complete
        signup_complete(message)


    # ! signup_complete
    def signup_complete(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_schedule = types.KeyboardButton("📰 Schedule")
        keyboard.add(item_schedule)
        bot.send_message(message.chat.id, "Ok, I got it", parse_mode="Markdown", reply_markup=keyboard)


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
        # ! schedule
        elif message.text == "📰 Schedule":
            bot.send_message(message.chat.id, "*Schedule of your patients:*", parse_mode="Markdown")
            fr = open("apoInfo.txt", "r")
            toRead = fr.read()
            print(toRead)
            fr.close()
            bot.send_message(message.chat.id, toRead, parse_mode="Markdown")
            # bot.send_message(message.chat.id, "*Name:* fullName, *Date:* date, *Time:* time", parse_mode="Markdown")


    # ! polling
    bot.infinity_polling()
    
    time.sleep(1)