from flask import Flask, request
from typing import ItemsView
from telebot import types
import telebot

TOKEN = "2142529380:AAH9OvlYi9zcii99FWijDrQiVhwGOjuFRn0"
bot = telebot.TeleBot(TOKEN)

# ! start
@bot.message_handler(commands=["start", "help"])
def start_message(message):
    # remove keyboard
    remove_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "*Привіт, {0.first_name}!👋*".format(message.from_user, bot.get_me()), reply_markup=remove_keyboard, parse_mode="Markdown")
    bot.send_message(message.chat.id, "*Якщо ти лікар, то тут ти можеш переглянути розклад своїх пацієнтів*", parse_mode="Markdown")
    global msg
    msg = bot.send_message(message.chat.id, "Напиши мені своє *ім'я* та *прізвище*", parse_mode="Markdown")
    bot.register_next_step_handler(msg, verification)

# ! buttons
@bot.message_handler(content_types=["text"])
def change_name(message):
    # ! change name
    if message.text == "✒️ Змінити ім'я":
        # delete
        bot.delete_message(message.chat.id, message.message_id)

        # remove keyboard
        remove_keyboard = types.ReplyKeyboardRemove()

        global msg
        msg = bot.send_message(message.chat.id, "Напиши мені своє *ім'я* та *прізвище*", reply_markup=remove_keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, verification)

    # ! schedule
    elif message.text == "📰 Розклад":
        # delete
        bot.delete_message(message.chat.id, message.message_id)

        bot.send_message(message.chat.id, "*Розклад твоїх пацієнтів:*", parse_mode="Markdown")

        # example
        bot.send_message(message.chat.id, "Пацієнт 1")
        bot.send_message(message.chat.id, "Пацієнт 2")
        bot.send_message(message.chat.id, "Пацієнт 3")

# ! verification
def verification(message):
    # add inline
    markup_inline_yn = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text="Так", callback_data="yes")
    item_no = types.InlineKeyboardButton(text="Ні", callback_data="no")
    markup_inline_yn.add(item_yes, item_no)

    bot.send_message(message.chat.id, f"*Тебе звати {message.text}?*", reply_markup=markup_inline_yn, parse_mode="Markdown")
# ! verification_complete
@bot.callback_query_handler(func=lambda call: True)
def verification_complete(call):
    if call.data == "yes":
        # add keyboard
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_change_name = types.KeyboardButton("✒️ Змінити ім'я")
        item_schedule = types.KeyboardButton("📰 Розклад")
        keyboard.add(item_change_name, item_schedule)

        bot.send_message(call.message.chat.id, "*Вибери, що робити далі*", reply_markup=keyboard, parse_mode="Markdown")
    elif call.data == "no":
        # remove keyboard
        remove_keyboard = types.ReplyKeyboardRemove()

        global msg
        msg = bot.send_message(call.message.chat.id, "Напиши мені своє *ім'я* та *прізвище*", reply_markup=remove_keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(msg, verification)

    # delete
    bot.delete_message(call.message.chat.id, call.message.message_id)

# ! polling
bot.infinity_polling()