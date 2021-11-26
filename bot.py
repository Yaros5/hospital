from typing import ItemsView
import telebot
from telebot import types

TOKEN = "2142529380:AAH9OvlYi9zcii99FWijDrQiVhwGOjuFRn0"
bot = telebot.TeleBot(TOKEN)

# ! start
@bot.message_handler(commands=["start", "help"])
def start_message(message):
    bot.send_message(message.chat.id, "Привіт, {0.first_name}!👋".format(
        message.from_user, bot.get_me()), parse_mode="html")
    bot.send_message(message.chat.id, "Якщо ти лікар, то тут ти можеш переглянути розклад своїх пацієнтів")
    msg = bot.send_message(message.chat.id, "Напиши мені своє ім'я та прізвише")
    bot.register_next_step_handler(msg, verification)

# ! change_name
@bot.message_handler(commands=["change_name"])
def change_name(message):
    msg = bot.send_message(message.chat.id, "Напиши мені своє ім'я та прізвише")
    bot.register_next_step_handler(msg, verification)

# ! verification
def verification(message):
   markup_inline_yn = types.InlineKeyboardMarkup()
   item_yes = types.InlineKeyboardButton(text = "Так", callback_data = "yes")
   item_no = types.InlineKeyboardButton(text = "Ні", callback_data = "no")
   markup_inline_yn.add(item_yes, item_no)
   bot.send_message(message.chat.id, f"Тебе звати {message.text}?", reply_markup=markup_inline_yn)

# ! verification_complete
@bot.callback_query_handler(func = lambda call: True)
def verification_complete(call):
    if call.data == "yes":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_change_name = types.KeyboardButton("Змінити ім'я")
        item_schedule = types.KeyboardButton("Розкдад")
        keyboard.add(item_change_name, item_schedule)
        bot.send_message(call.message.chat.id, "Вибери, що робити далі", reply_markup = keyboard)
    elif call.data == "no":
        bot.register_next_step_handler(verification)

bot.infinity_polling()