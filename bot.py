from typing import ItemsView

from nacl import secret
from telebot import types
import telebot

TOKEN = "2142529380:AAH9OvlYi9zcii99FWijDrQiVhwGOjuFRn0"
bot = telebot.TeleBot(TOKEN)

# ! start
@bot.message_handler(commands=["start", "help"])
def start_message(message):
    bot.remove_webhook()
    # remove keyboard
    remove_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "*Hello, {0.first_name} 👋*".format(message.from_user, bot.get_me()), reply_markup=remove_keyboard, parse_mode="Markdown")
    bot.send_message(message.chat.id, "*If you are a doctor, then you can view the schedule of your patients here*", parse_mode="Markdown")
    change_name(message)

# ! change name
def change_name(message):
    # remove keyboard
    remove_keyboard = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, "Send me your *full name*", parse_mode="Markdown", reply_markup=remove_keyboard)
    bot.register_next_step_handler(msg, verification)

# ! verification
def verification(message):
    bot.send_message(message.chat.id, f"*Your name is {message.text}*", parse_mode="Markdown")
    login_from_bot = message.text
    print(f"User login from bot: {login_from_bot}")


# ! buttons
@bot.message_handler(content_types=["text"])
def buttons(message):
    # ! ADMIN
    # / remove webhook
    if message.text == "remove_webhook":
        bot.delete_message(message.chat.id, message.message_id)
        bot.remove_webhook()
    / stop polling
    elif message.text == "stop_polling":
        bot.delete_message(message.chat.id, message.message_id)
        bot.stop_bot()
    / secret
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